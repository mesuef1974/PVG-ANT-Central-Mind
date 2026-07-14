#!/usr/bin/env python3
"""Create the single PASS023 summary figure from the reproducible JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt


COLORS = ["#0B5CAD", "#2E77B8", "#6BAED6", "#9ECAE1"]
MARKERS = ["o", "s", "^", "D"]
LINESTYLES = ["-", "--", "-.", ":"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "results" / "avrg_pass023_results.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "figures" / "avrg_pass023_mean_ratio_by_modulus.png",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))

    fig, ax = plt.subplots(figsize=(10, 6), dpi=180)
    for index, window in enumerate(data["windows"]):
        xs = [row["r"] for row in window["per_modulus"]]
        ys = [row["mean_ratio"] for row in window["per_modulus"]]
        exp = window["exp"]
        ax.plot(
            xs,
            ys,
            color=COLORS[index],
            marker=MARKERS[index],
            linestyle=LINESTYLES[index],
            linewidth=1.8,
            markersize=5.5,
            markeredgecolor="#17324D",
            markeredgewidth=0.6,
            label=rf"$e={exp}$: $[2^{{{exp}}},2^{{{exp + 1}}})$",
        )

    ax.axhline(2.0, color="#303841", linewidth=1.4, linestyle=(0, (5, 4)))
    ax.text(31.35, 2.008, "reference = 2", color="#303841", fontsize=9)
    fig.suptitle(
        "Mean on/off energy ratio by prime modulus",
        x=0.07,
        y=0.985,
        ha="left",
        fontsize=15,
    )
    fig.text(
        0.07,
        0.945,
        "Four full even-N windows; conjugate-pair representatives; focused y-scale",
        fontsize=9.5,
        color="#56616B",
    )
    ax.set_xlabel("Prime modulus r")
    ax.set_ylabel("Mean energy ratio")
    ax.set_xticks(data["configuration"]["moduli"])
    ax.set_xlim(4.2, 33.2)
    ax.set_ylim(1.85, 3.16)
    ax.grid(axis="y", color="#D9DEE3", linewidth=0.7)
    ax.grid(axis="x", visible=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#66717A")
    ax.spines["bottom"].set_color("#66717A")
    ax.tick_params(colors="#38434D")
    ax.legend(frameon=False, ncol=2, loc="upper right", fontsize=8.5)
    fig.tight_layout(rect=[0, 0, 1, 0.91])
    fig.savefig(args.output, bbox_inches="tight", facecolor="white")
    print(f"PASS023 figure: {args.output}")


if __name__ == "__main__":
    main()
