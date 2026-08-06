from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STATUS = ROOT / 'research/avrg-axis-sum/governance/ACTIVE-001-F-EXACT-MULTI-MODULUS-RANK-STATUS-v1.1.md'
REPORT = ROOT / 'research/research-memory-graph/governance/RMG-GOV-006-FIRST-P0-SOURCE-MIGRATION.md'

required_status = [
    'assimilation_level = ASSIM-L5',
    'math_contribution_level = MATH-M1',
    'operational_maturity = OPS-REGRESSION-TESTED',
    'certificate_strength = CERT-FINITE',
    'pvg_necessity_level = PVG-N1',
    'prior_art_status = UNVERIFIED',
    'Goldbach/RH/GRH progress: `NONE`',
]

errors = []
for path in (STATUS, REPORT):
    if not path.exists():
        errors.append(f'missing: {path}')

if STATUS.exists():
    text = STATUS.read_text(encoding='utf-8')
    for token in required_status:
        if token not in text:
            errors.append(f'missing status token: {token}')
    if 'originality/priority: `NOT AUTHORIZED`' not in text:
        errors.append('historical novelty ceiling was lost')

if REPORT.exists():
    report = REPORT.read_text(encoding='utf-8')
    for token in ('theorem validity: unchanged', 'repository-wide compliance', 'PVG-N1'):
        if token not in report:
            errors.append(f'missing report token: {token}')

if errors:
    raise SystemExit('\n'.join(errors))
print('PASS RMG-GOV-006 static source-migration checks')
