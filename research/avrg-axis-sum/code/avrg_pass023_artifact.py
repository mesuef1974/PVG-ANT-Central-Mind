#!/usr/bin/env python3
"""Build the canonical portable Data Analytics artifact for PASS023."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / "results" / "avrg_pass023_results.json"
OUTPUT = HERE.parent / "results" / "avrg_pass023_artifact.json"
GENERATED_AT = "2026-07-14T12:00:00Z"
TITLE = "AVRG PASS023 — ثبات النوافذ المتعددة والمعايير الأكبر"


def build(data: dict) -> dict:
    mean_ratios = []
    for window in data["windows"]:
        for row in window["per_modulus"]:
            mean_ratios.append(
                {
                    "exp": window["exp"],
                    "window": f"[2^{window['exp']}, 2^{window['exp'] + 1})",
                    "r": row["r"],
                    "mean_ratio": row["mean_ratio"],
                    "population_sd": row["population_sd"],
                    "representative_count": row["representative_count"],
                    "min_ratio": row["min_ratio"],
                    "max_ratio": row["max_ratio"],
                }
            )

    cross_modulus = [
        {
            "r": row["r"],
            "cross_window_mean": row["cross_window_mean"],
            "between_window_sd": row["cross_window_population_sd"],
            "mean_within_character_sd": row["mean_within_modulus_population_sd"],
            "mean_absolute_deviation_from_two": row[
                "mean_absolute_deviation_from_two"
            ],
        }
        for row in data["cross_window"]["per_modulus"]
    ]
    larger = [
        {
            **row,
            "moduli": ",".join(str(value) for value in row["moduli"]),
        }
        for row in data["cross_window"]["larger_moduli_by_window"]
    ]
    models = data["cross_window"]["model_preference_by_window"]
    thresholds = [
        {
            **row,
            "moduli": ",".join(str(value) for value in row["moduli"]),
        }
        for row in data["cross_window"]["aggregate_threshold_sensitivity"]
    ]

    mean_values = ",\n    ".join(
        "(" + ", ".join(
            [
                str(row["exp"]),
                str(row["r"]),
                format(row["mean_ratio"], ".17g"),
                "'" + row["window"].replace("'", "''") + "'",
            ]
        ) + ")"
        for row in mean_ratios
    )
    mean_sql = (
        "WITH pass023_mean_ratios(exp, r, mean_ratio, window_label) AS (\n"
        f"  VALUES\n    {mean_values}\n"
        ")\n"
        "SELECT exp, r, mean_ratio, window_label AS window\n"
        "FROM pass023_mean_ratios\nORDER BY exp, r"
    )
    cross_values = ",\n    ".join(
        "(" + ", ".join(
            [
                str(row["r"]),
                format(row["cross_window_mean"], ".17g"),
                format(row["between_window_sd"], ".17g"),
                format(row["mean_within_character_sd"], ".17g"),
                format(row["mean_absolute_deviation_from_two"], ".17g"),
            ]
        ) + ")"
        for row in cross_modulus
    )
    cross_sql = (
        "WITH pass023_cross_modulus(r, cross_window_mean, between_window_sd, "
        "mean_within_character_sd, mean_absolute_deviation_from_two) AS (\n"
        f"  VALUES\n    {cross_values}\n"
        ")\nSELECT * FROM pass023_cross_modulus\nORDER BY r"
    )

    source_manifests = [
        {
            "id": "pass023_mean_ratios",
            "label": "PASS023 window-by-modulus means",
            "path": "avrg_pass023_results.json",
        },
        {
            "id": "pass023_cross_modulus",
            "label": "PASS023 cross-window modulus summary",
            "path": "avrg_pass023_results.json",
        },
    ]

    def source(manifest_source: dict, sql: str, description: str) -> dict:
        return {
            **manifest_source,
            "query": {
                "engine": "portable-sql",
                "sql": sql,
                "description": description,
                "executed_at": GENERATED_AT,
                "tables_used": ["inline VALUES derived from avrg_pass023_results.json"],
                "filters": [
                    "exp in {15,16,17,18}",
                    "r in {5,7,11,13,17,19,23,29,31}",
                    "even nonprincipal characters; conjugate pairs collapsed",
                ],
                "metric_definitions": [
                    "mean_ratio: arithmetic mean of on_energy/off_energy over retained character representatives",
                    "between_window_sd: population standard deviation of a modulus mean over four windows",
                    "mean_within_character_sd: mean population standard deviation across characters within each window",
                ],
            },
        }

    sources = [
        source(
            source_manifests[0],
            mean_sql,
            "Exact portable SQL projection of the 36 window-by-modulus means computed by PASS023.",
        ),
        source(
            source_manifests[1],
            cross_sql,
            "Exact portable SQL projection of the nine cross-window modulus summaries computed by PASS023.",
        ),
    ]

    manifest = {
        "version": 1,
        "surface": "report",
        "title": TITLE,
        "description": (
            "Finite computational evidence for mean-ratio stability near 2, "
            "with explicit sensitivity and character-dispersion caveats."
        ),
        "generatedAt": GENERATED_AT,
        "charts": [
            {
                "id": "mean_ratio_by_modulus",
                "title": "متوسط النسبة بحسب المعيار والنافذة",
                "subtitle": "المعيار r=5 مرتفع النفوذ؛ المعايير الأكبر تتجمع قرب 2 دون رتابة.",
                "type": "line",
                "dataset": "mean_ratios",
                "sourceId": "pass023_mean_ratios",
                "encodings": {
                    "x": {"field": "r", "type": "quantitative", "label": "المعيار r"},
                    "y": {
                        "field": "mean_ratio",
                        "type": "quantitative",
                        "label": "متوسط نسبة on/off",
                        "format": ".4f",
                    },
                    "color": {"field": "window", "type": "nominal", "label": "النافذة"},
                },
                "yAxisTitle": "متوسط النسبة",
                "valueFormat": ".4f",
                "layout": "full",
            }
        ],
        "tables": [
            {
                "id": "cross_modulus_table",
                "title": "ملخص كل معيار عبر النوافذ الأربع",
                "subtitle": "التشتت داخل الشخصية يبقى محسوسًا حتى حين يستقر المتوسط.",
                "dataset": "cross_modulus",
                "sourceId": "pass023_cross_modulus",
                "defaultSort": {"field": "r", "direction": "asc"},
                "density": "dense",
                "layout": "full",
                "columns": [
                    {"field": "r", "label": "r", "type": "number"},
                    {"field": "cross_window_mean", "label": "متوسط النوافذ", "format": ".6f"},
                    {"field": "between_window_sd", "label": "SD بين النوافذ", "format": ".6f"},
                    {"field": "mean_within_character_sd", "label": "SD داخل المعيار", "format": ".6f"},
                    {"field": "mean_absolute_deviation_from_two", "label": "متوسط |ρ̄−2|", "format": ".6f"},
                ],
            }
        ],
        "sources": source_manifests,
        "blocks": [
            {"id": "title", "type": "markdown", "body": f"# {TITLE}"},
            {
                "id": "summary",
                "type": "markdown",
                "body": (
                    "## الخلاصة\n\nتدعم النوافذ الأربع حدسًا تجريبيًا محدودًا: متوسط النسبة "
                    "يتجمع قرب **2** للمعايير الأكبر المختبرة. لا يوجد برهان تقاربي، "
                    "ولا تقدم مباشر نحو إثبات غولدباخ."
                ),
            },
            {
                "id": "scope",
                "type": "markdown",
                "body": (
                    "## النطاق\n\nأربع نوافذ كاملة، وتسعة معايير أولية، و136 نسبة ممثلة. "
                    "نجحت المعايرة على 15 صفًا بأقصى فرق مطلق `8.88e-16`."
                ),
            },
            {"id": "chart", "type": "chart", "chartId": "mean_ratio_by_modulus", "layout": "full"},
            {
                "id": "finding",
                "type": "markdown",
                "body": (
                    "## النتيجة الرئيسة\n\nللمعايير 23 و29 و31 تراوح متوسط متوسطات المعايير "
                    "عبر النوافذ بين **1.9878** و**2.0256**. مع ذلك بقي تشتت الشخصيات "
                    "داخل المعيار غير تافه؛ الاستقرار يخص المتوسط لا كل شخصية."
                ),
            },
            {"id": "table", "type": "table", "tableId": "cross_modulus_table", "layout": "full"},
            {
                "id": "sensitivity",
                "type": "markdown",
                "body": (
                    "## حساسية المعيار الصغير\n\nالمعيار `r=5` استثنائي بمتوسط عبر النوافذ "
                    "**2.7543**. يتغير الجزء المقطوع الحر المجمع من 1.8119 لكل المعايير "
                    "إلى 1.9727 بعد اشتراط `r≥7`؛ هذه حساسية وصفية لا تقدير حد."
                ),
            },
            {
                "id": "models",
                "type": "markdown",
                "body": (
                    "## مقارنة النماذج\n\nاختيار LOOCV يتناوب: نموذج الحد الثابت 2 في نافذتي "
                    "e=15 وe=18، والجزء المقطوع الحر في e=16 وe=17. لذلك لا تحسم "
                    "البيانات قانونًا تقاربيًا."
                ),
            },
            {
                "id": "limitations",
                "type": "markdown",
                "body": (
                    "## القيود\n\nالعينة نهائية وصغيرة، والعتبات استكشافية، والتطبيع يعتمد "
                    "على الحد الرئيسي Hardy–Littlewood المستخدم في المسار. لا يثبت التحليل "
                    "أن المتوسط يتقارب إلى 2، ولا تقاربًا منتظمًا في k، ولا حالة جديدة من غولدباخ."
                ),
            },
            {
                "id": "next",
                "type": "markdown",
                "body": (
                    "## الخطوة التالية\n\nPASS024: فصل مقياس المعيار عن تغاير الشخصية بنموذج "
                    "`ρ(e,r,k)=2+A_e/r+G_r(k)+ε` واختبار ثبات المركبة الشخصية بين النوافذ."
                ),
            },
        ],
    }
    return {
        "surface": "report",
        "manifest": manifest,
        "snapshot": {
            "version": 1,
            "generatedAt": GENERATED_AT,
            "status": "ready",
            "datasets": {
                "mean_ratios": mean_ratios,
                "cross_modulus": cross_modulus,
                "larger_moduli_windows": larger,
                "model_comparison": models,
                "threshold_sensitivity": thresholds,
            },
        },
        "sources": sources,
        "package_info": {
            "root": ".",
            "manifestPath": "avrg_pass023_artifact.json",
            "snapshotPath": "avrg_pass023_artifact.json",
            "sourceKind": "reproducible-python-computation",
        },
    }


def main() -> None:
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    artifact = build(data)
    OUTPUT.write_text(
        json.dumps(artifact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(OUTPUT)


if __name__ == "__main__":
    main()
