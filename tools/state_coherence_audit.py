#!/usr/bin/env python3
"""state_coherence_audit.py -- repository-truth checker (Coherence PASS).

Not a mathematical-completeness checker. It fails on stale-state contradictions
between the audits, book READMEs, registries, maps, governance, transition-memory,
and unit files — and (since State-Repair 006-C) runs a repo-wide stale-story sweep
over every tracked md/jsonl file: stale Montgomery story patterns are forbidden
outside explicit historical / superseded / quarantined contexts.

stdlib only. Run from anywhere: python tools/state_coherence_audit.py
"""
import os
import sys
import glob
import re
import json
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONT = "ledgers/books/BOOK-ANT-MONTGOMERY-MNT-II-004"


def read(rel):
    p = os.path.join(ROOT, rel)
    if not os.path.isfile(p):
        return None
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


issues = []


def need(cond, msg):
    if not cond:
        issues.append(msg)


def closure_pass(name):
    t = read(os.path.join("audits", name))
    return t is not None and "PASS" in t


def book_readme(book):
    return read(os.path.join("ledgers/books", book, "README.md")) or ""


# 1. root README mentions the current phase
readme = read("README.md") or ""
need(("Coherence Audit 005" in readme) or ("v0.6" in readme),
     "README.md does not mention the current phase (Coherence Audit 005 / v0.6)")

# 2/3. transition memory must track the LIVE goal registry, not an era token.
# (GOVERNANCE-ENFORCEMENT-CLOSURE-001: the previous checks pinned these files to
#  v0.6/Montgomery-era strings and reported false staleness forever after the
#  compass-v1.0 transition. The replacement derives the expectation from
#  registries/program-goals.jsonl: every ACTIVE operational goal must be named
#  in both latest-state and next-action. Era-neutral and strictly registry-driven.)
latest = read("transition-memory/latest-state.md") or ""
nexta = read("transition-memory/next-action.md") or ""
active_op_goals = []
for line in (read("registries/program-goals.jsonl") or "").splitlines():
    if not line.strip():
        continue
    try:
        g = json.loads(line)
    except Exception:
        continue
    if str(g.get("id", "")).startswith("GOAL-OP-") and str(g.get("status", "")).startswith("active"):
        active_op_goals.append(g["id"])
need(bool(active_op_goals),
     "registries/program-goals.jsonl declares no active operational goal")
for gid in active_op_goals:
    need(gid in latest,
         "transition-memory/latest-state.md omits active operational goal %s" % gid)
    need(gid in nexta,
         "transition-memory/next-action.md omits active operational goal %s" % gid)

# 8. planned.jsonl empty must be reflected in next-action
planned = read("registries/planned.jsonl") or ""
if planned.strip() == "":
    need("planned.jsonl" in nexta,
         "planned.jsonl is empty but transition-memory/next-action.md does not reflect it")

# 4/5/6. closure PASS must not coexist with a scope-open / awaiting book README
if closure_pass("v0.2-B-closure.md"):
    need("awaiting" not in book_readme("BOOK-LOGIC-MILETI-001").lower(),
         "Mileti README says 'awaiting' but v0.2-B-closure.md is PASS")
if closure_pass("v0.4-closure.md"):
    t = book_readme("BOOK-ANT-IWANIEC-KOWALSKI-003").lower()
    need("scope open" not in t and "scope_open" not in t and "awaiting" not in t,
         "IK README says 'scope open'/'awaiting' but v0.4-closure.md is PASS")
if closure_pass("v0.5-closure.md"):
    t = book_readme("BOOK-SIEVE-HARMAN-004").lower()
    need("scope open" not in t and "scope_open" not in t and "awaiting" not in t,
         "Harman README says 'scope open'/'awaiting' but v0.5-closure.md is PASS")

# Montgomery: which units actually exist
unit_files = sorted(glob.glob(os.path.join(ROOT, MONT, "units", "MNTII-006-*.md")))
letters = []
for u in unit_files:
    m = re.search(r"MNTII-006-([A-Z])\.md$", os.path.basename(u))
    if m:
        letters.append(m.group(1))
mont_readme = read(os.path.join(MONT, "README.md")) or ""

# 7. Montgomery README must mention every existing unit
for L in letters:
    need(("006-%s" % L) in mont_readme,
         "Montgomery README does not mention existing unit %s" % L)

# 9. no stale 'No MNTII-006-<L>' for a unit that exists
for p in glob.glob(os.path.join(ROOT, MONT, "*.md")) + glob.glob(os.path.join(ROOT, MONT, "units", "*.md")):
    with open(p, encoding="utf-8", errors="replace") as f:
        t = f.read()
    for L in letters:
        need(("No MNTII-006-%s" % L) not in t,
             "stale 'No MNTII-006-%s' in %s while that unit exists" % (L, os.path.relpath(p, ROOT)))

# 10. registry book status must not contradict unit/audit files
books = read("registries/books.jsonl") or ""
mont_line = ""
for line in books.splitlines():
    if "BOOK-ANT-MONTGOMERY-MNT-II-004" in line:
        mont_line = line
# Book-overlay closure authorization (AUDIT-CM-MONTGOMERY-OVERLAY-008):
# the overlay may be marked closed ONLY on the authorizing audit's recommendation.
overlay_audit_txt = read("audits/montgomery-post-h-overlay-audit-008.md")
OVERLAY_AUTHORIZED = (overlay_audit_txt is not None
                      and "RECOMMEND book_overlay_closed" in overlay_audit_txt)
MONT_OVERLAY_CLOSED = '"status": "book_overlay_closed"' in mont_line

if letters:
    need('"status": "scope_open"' not in mont_line,
         "books.jsonl Montgomery status is still 'scope_open' but units exist")
    if MONT_OVERLAY_CLOSED:
        need(OVERLAY_AUTHORIZED,
             "books.jsonl Montgomery is book_overlay_closed without the authorizing overlay audit")
    else:
        need("partial_overlay" in mont_line,
             "books.jsonl Montgomery should be 'partial_overlay' (has units, overlay in progress)")

# SOURCE-GROUNDING CORRECTION 006 invariants (source is the governor, not miner speed)
try:
    obj = json.loads(mont_line) if mont_line.strip() else {}
except Exception:
    obj = {}
trusted = str(obj.get("trusted_source_units", "")) or str(obj.get("trusted_closed_units", ""))
quarant = str(obj.get("quarantined_units", ""))
trusted_tokens = [t.strip() for t in trusted.replace("+", ",").split(",") if t.strip()]
# A and B must NOT be counted as trusted source-grounded units (cross-volume source-mismatch)
need("A" not in trusted_tokens, "books.jsonl counts quarantined unit A among trusted source units")
need("B" not in trusted_tokens, "books.jsonl counts quarantined unit B among trusted source units")
# A and B must be marked quarantined
need("A" in quarant, "books.jsonl does not mark unit A quarantined (source-mismatch)")
need("B" in quarant, "books.jsonl does not mark unit B quarantined (source-mismatch)")
# The legacy off-diagonal E must not be trusted; it must be quarantined
need("legacy" not in trusted.lower(), "books.jsonl counts the legacy off-diagonal E among trusted units")
need("legacy" in quarant.lower(), "books.jsonl does not mark the legacy off-diagonal E quarantined")
# Montgomery must not be called a full book closure UNLESS the overlay audit authorized it
if not OVERLAY_AUTHORIZED:
    need(obj.get("status") != "book_overlay_closed"
         and "closed" not in str(obj.get("overlay", "")).lower(),
         "books.jsonl Montgomery is marked as a full book closure; must be partial_overlay")
# E closure state machine: BEFORE a v0.6-e-closure PASS, E = validated_intake NOT closed;
# AFTER it, E must be marked CLOSED and every layer must reflect the closure.
e_closure_txt = read(os.path.join("audits", "v0.6-e-closure.md"))
E_CLOSED = e_closure_txt is not None and "PASS" in e_closure_txt
if e_closure_txt is not None:
    need("PASS" in e_closure_txt,
         "audits/v0.6-e-closure.md exists but does not record PASS")
e_intake = read(os.path.join(MONT, "units", "MNTII-006-E.md")) or ""
if e_intake:
    if E_CLOSED:
        need(re.search(r"\*\*Status:\*\*\s*CLOSED", e_intake),
             "v0.6-e-closure PASS exists but MNTII-006-E is not marked Status: CLOSED")
        # stale live-state claims about closed units are caught by the repo-wide
        # closed-unit scan below (State-Repair 006-D) — no file whitelist here.
    else:
        need(not re.search(r"\*\*Status:\*\*\s*CLOSED", e_intake),
             "MNTII-006-E is marked Status: CLOSED but no v0.6-e-closure PASS exists")
        need(re.search(r"\*\*Status:\*\*[^\n]*validated_intake", e_intake),
             "MNTII-006-E (intake) Status line is not validated_intake")
        need("not closed" in e_intake.lower(), "MNTII-006-E (intake) is not marked NOT closed")
# F state machine: F may exist ONLY as the packet-grounded Ch-17 unit selected via
# Coverage Audit 007; before a v0.6-f-closure PASS it stays validated_intake NOT closed.
f_txt = read(os.path.join(MONT, "units", "MNTII-006-F.md"))
if f_txt is not None:
    need(os.path.isfile(os.path.join(ROOT, "audits", "montgomery-book-coverage-audit-007.md")),
         "MNTII-006-F exists without the coverage audit that authorized its selection")
    need("Treasure Packet" in f_txt and "Ch 17" in f_txt,
         "MNTII-006-F is not grounded in the Ch-17 Treasure Packet")
    f_closure = read(os.path.join("audits", "v0.6-f-closure.md"))
    F_CLOSED = f_closure is not None and "PASS" in f_closure
    if f_closure is not None:
        need("PASS" in f_closure, "audits/v0.6-f-closure.md exists but does not record PASS")
    if F_CLOSED:
        need(re.search(r"\*\*Status:\*\*\s*CLOSED", f_txt),
             "v0.6-f-closure PASS exists but MNTII-006-F is not marked Status: CLOSED")
    else:
        need(not re.search(r"\*\*Status:\*\*\s*CLOSED", f_txt),
             "MNTII-006-F is marked Status: CLOSED but no v0.6-f-closure PASS exists")
        need(re.search(r"\*\*Status:\*\*[^\n]*validated_intake", f_txt),
             "MNTII-006-F (intake) Status line is not validated_intake")
        need("not closed" in f_txt.lower(), "MNTII-006-F (intake) is not marked NOT closed")
# G state machine: G may exist ONLY as the packet-grounded Ch-16 support unit (selection
# recorded at 4a042b5); before a v0.6-g-closure PASS it stays validated_intake NOT closed.
g_txt = read(os.path.join(MONT, "units", "MNTII-006-G.md"))
if g_txt is not None:
    need("Treasure Packet" in g_txt and "Ch 16" in g_txt,
         "MNTII-006-G is not grounded in the Ch-16 Treasure Packet")
    need("legacy" in g_txt.lower(),
         "MNTII-006-G does not carry the no-legacy-E-revival guard note")
    g_closure = read(os.path.join("audits", "v0.6-g-closure.md"))
    G_CLOSED = g_closure is not None and "PASS" in g_closure
    if g_closure is not None:
        need("PASS" in g_closure, "audits/v0.6-g-closure.md exists but does not record PASS")
    if G_CLOSED:
        need(re.search(r"\*\*Status:\*\*\s*CLOSED", g_txt),
             "v0.6-g-closure PASS exists but MNTII-006-G is not marked Status: CLOSED")
    else:
        need(not re.search(r"\*\*Status:\*\*\s*CLOSED", g_txt),
             "MNTII-006-G is marked Status: CLOSED but no v0.6-g-closure PASS exists")
        need(re.search(r"\*\*Status:\*\*[^\n]*validated_intake", g_txt),
             "MNTII-006-G (intake) Status line is not validated_intake")
        need("not closed" in g_txt.lower(), "MNTII-006-G (intake) is not marked NOT closed")
        need(any(tok.startswith("G") for tok in trusted_tokens),
             "books.jsonl trusted_source_units omits the G intake while units/MNTII-006-G.md exists")
        need("TOOL-MONTGOMERY-VDC-EXPONENTIAL-SUMS-DIAGNOSTIC-001" in (read("maps/current-capabilities.md") or ""),
             "maps/current-capabilities.md omits the G-intake tool")
        need("MNTII-006-G" in (read(os.path.join(MONT, "missed-treasures.md")) or ""),
             "missed-treasures.md omits MNTII-006-G")
        need("v0.6-G Closure Review" in readme,
             "root README.md does not point to the v0.6-G Closure Review track")
# H state machine: H may exist ONLY as the packet-grounded Ch-18 application unit;
# before a v0.6-h-closure PASS it stays validated_intake NOT closed.
h_txt = read(os.path.join(MONT, "units", "MNTII-006-H.md"))
if h_txt is not None:
    need("Treasure Packet" in h_txt and "Ch 18" in h_txt,
         "MNTII-006-H is not grounded in the Ch-18 Treasure Packet")
    need("binary Goldbach" in h_txt and "open" in h_txt.lower(),
         "MNTII-006-H does not carry the binary-Goldbach-is-OPEN fencing")
    h_closure = read(os.path.join("audits", "v0.6-h-closure.md"))
    H_CLOSED = h_closure is not None and "PASS" in h_closure
    if h_closure is not None:
        need("PASS" in h_closure, "audits/v0.6-h-closure.md exists but does not record PASS")
    if H_CLOSED:
        need(re.search(r"\*\*Status:\*\*\s*CLOSED", h_txt),
             "v0.6-h-closure PASS exists but MNTII-006-H is not marked Status: CLOSED")
    else:
        need(not re.search(r"\*\*Status:\*\*\s*CLOSED", h_txt),
             "MNTII-006-H is marked Status: CLOSED but no v0.6-h-closure PASS exists")
        need(re.search(r"\*\*Status:\*\*[^\n]*validated_intake", h_txt),
             "MNTII-006-H (intake) Status line is not validated_intake")
        need("not closed" in h_txt.lower(), "MNTII-006-H (intake) is not marked NOT closed")
        need(any(tok.startswith("H") for tok in trusted_tokens),
             "books.jsonl trusted_source_units omits the H intake while units/MNTII-006-H.md exists")
        need("TOOL-MONTGOMERY-ADDITIVE-PRIME-CIRCLE-METHOD-DIAGNOSTIC-001" in (read("maps/current-capabilities.md") or ""),
             "maps/current-capabilities.md omits the H-intake tool")
        need("MNTII-006-H" in (read(os.path.join(MONT, "missed-treasures.md")) or ""),
             "missed-treasures.md omits MNTII-006-H")
        need("v0.6-H Closure Review" in readme,
             "root README.md does not point to the v0.6-H Closure Review track")
# no MNTII-006-I (no further unit without a packet and explicit permission;
# after the H closure the next step is a post-H coverage/overlay audit, not unit I)
need(not os.path.isfile(os.path.join(ROOT, MONT, "units", "MNTII-006-I.md")),
     "MNTII-006-I unit exists; no further Montgomery unit is allowed without a packet and permission")

# STATE-REPAIR 006-B invariants: quarantine must propagate to tools.jsonl and maps/
QUARANTINED_TOOLS = (
    "TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001",   # unit A
    "TOOL-MONTGOMERY-DISTRIBUTION-BARRIER-001",      # unit B
    "TOOL-MONTGOMERY-EXPSUM-DIAGNOSTIC-001",         # legacy off-diagonal E
)
BOUNDED_GAPS_TOOL = "TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001"
tools_by_id = {}
for line in (read("registries/tools.jsonl") or "").splitlines():
    if not line.strip():
        continue
    try:
        t = json.loads(line)
        tools_by_id[t.get("id", "")] = t
    except Exception:
        pass
for tid in QUARANTINED_TOOLS:
    t = tools_by_id.get(tid)
    need(t is not None,
         "tools.jsonl: quarantined tool %s is missing (quarantine history must not be erased)" % tid)
    if t is None:
        continue
    need(t.get("status") == "quarantined_source_mismatch",
         "tools.jsonl: %s is not stamped status=quarantined_source_mismatch" % tid)
    need("quarantin" in str(t.get("role", "")).lower(),
         "tools.jsonl: %s role does not carry the quarantine marker (treated as live/trusted)" % tid)
bg = tools_by_id.get(BOUNDED_GAPS_TOOL)
need(bg is not None, "tools.jsonl: bounded-gaps tool %s is missing" % BOUNDED_GAPS_TOOL)
if bg is not None:
    need(bg.get("status") != "quarantined_source_mismatch",
         "tools.jsonl: bounded-gaps tool is wrongly quarantined")

caps = read("maps/current-capabilities.md")
need(caps is not None, "maps/current-capabilities.md is missing")
if caps is not None:
    need(BOUNDED_GAPS_TOOL in caps,
         "maps/current-capabilities.md does not list the bounded-gaps tool (capability map stale)")
    need("pre-packet" not in caps,
         "maps/current-capabilities.md still carries the stale 'pre-packet' E description")
    cap_lines = caps.splitlines()
    for i, ln in enumerate(cap_lines):
        # every mention of a quarantined tool must sit inside a QUARANTINED-marked window
        for tid in QUARANTINED_TOOLS:
            if tid in ln:
                window = " ".join(cap_lines[max(0, i - 2):i + 1]).lower()
                need("quarantin" in window,
                     "maps/current-capabilities.md lists quarantined tool %s as installed live" % tid)
        # the new E must not be called quarantined/unvalidated (only the legacy E may be)
        low = ln.lower()
        if "mntii-006-e" in low and ("quarantin" in low or "unvalidated" in low):
            need("legacy" in low or "not quarantin" in low,
                 "maps/current-capabilities.md calls the new MNTII-006-E quarantined/unvalidated")
    if E_CLOSED:
        need("v0.6-e-closure" in caps,
             "maps/current-capabilities.md does not reflect the closed E (v0.6-e-closure PASS)")
    else:
        need("validated_intake" in caps,
             "maps/current-capabilities.md does not record the new E as validated_intake")
# The state files must carry the quarantine / source-mismatch markers
qwords = ("quarantin", "source-mismatch", "unvalidated", "pre-packet")
for rel in [os.path.join(MONT, "README.md"), "registries/books.jsonl", "transition-memory/next-action.md"]:
    t = (read(rel) or "").lower()
    need(any(q in t for q in qwords),
         "%s does not carry the quarantine / source-mismatch markers" % rel)

# ---- STATE-REPAIR 006-C: repo-wide stale-story sweep -------------------------
# Every tracked md/jsonl file must tell the legal Montgomery story. Stale-story
# patterns are allowed ONLY inside explicit historical / superseded / quarantined
# contexts (audits/, units/_quarantine/, or a marked line/window).

def story_files():
    files = []
    try:
        r = subprocess.run(["git", "ls-files"], cwd=ROOT,
                           capture_output=True, text=True, timeout=30)
        if r.returncode == 0:
            files = [f.strip() for f in r.stdout.splitlines() if f.strip()]
    except Exception:
        files = []
    if not files:  # fallback: filesystem walk minus non-repo dirs
        for dp, dns, fns in os.walk(ROOT):
            dns[:] = [d for d in dns if d not in
                      (".git", "Books_others", ".venv", ".idea", "node_modules")]
            for fn in fns:
                files.append(os.path.relpath(os.path.join(dp, fn), ROOT).replace(os.sep, "/"))
    return [f for f in files if f.endswith((".md", ".jsonl"))]


HIST_LINE_TOKENS = ("historical", "supersed", "stale", "blocked review",
                    "legacy", "not quarantin", "quarantined legacy")


def line_in_historical_context(lines, i):
    w = " ".join(lines[max(0, i - 3):i + 1]).lower()
    return any(tok in w for tok in HIST_LINE_TOKENS)


STALE_LINE_PATTERNS = [
    (re.compile(r"A[–-]D\s*(closed|مُغلَقة|مغلقة)"),
     "stale 'A-D closed' story (A/B are quarantined)"),
    (re.compile(r"A\s*\+\s*B\s*\+\s*C\s*\+\s*D"),
     "stale 'A+B+C+D trusted' story (A/B are quarantined)"),
    (re.compile(r"Next[:*\s]+MNTII-006-E\s+Intake"),
     "stale 'Next: E Intake' pointer (current next action is the v0.6-E Closure Review track)"),
    (re.compile(r"MNTII-006-F\s*:?\s*deferred"),
     "stale 'MNTII-006-F deferred' (F is NOT ALLOWED, not deferred)"),
]

QUAR_WORDS = ("quarantin", "pre-packet", "محجورة", "غير مُصدَّقة")

for rel in story_files():
    if rel.startswith("audits/") or "/_quarantine/" in rel:
        continue  # pinned historical records / quarantined legacy notes
    text = read(rel)
    if text is None:
        continue
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        low = ln.lower()
        for pat, msg in STALE_LINE_PATTERNS:
            if pat.search(ln) and not line_in_historical_context(lines, i):
                need(False, "%s:%d: %s" % (rel, i + 1, msg))
        # the new E must never be called quarantined/pre-packet without naming legacy-E
        if "mntii-006-e" in low and any(q in low for q in QUAR_WORDS):
            if not line_in_historical_context(lines, i):
                need(False,
                     "%s:%d: calls MNTII-006-E quarantined/pre-packet without specifying legacy-E" % (rel, i + 1))
        # Montgomery must never be called a full book closure in prose UNLESS authorized
        # (STRICT: only an explicit negation or a same-line historical marker exempts —
        #  the neighbourhood exemption was demonstrated to shield a live claim)
        if ("montgomery" in low or "mnt-ii" in low or "mntii" in low) and "book_overlay_closed" in low:
            if (not OVERLAY_AUTHORIZED and "not book_overlay" not in low
                    and "historical" not in low and "تاريخي" not in ln):
                need(False, "%s:%d: calls Montgomery book_overlay_closed" % (rel, i + 1))
        # a quarantined tool must not be presented live in navigation/truth layers
        if (rel == "README.md" or rel.startswith(("maps/", "transition-memory/", "governance/"))):
            for tid in QUARANTINED_TOOLS:
                if tid in ln:
                    w = " ".join(lines[max(0, i - 2):i + 1]).lower()
                    need("quarantin" in w,
                         "%s:%d: lists quarantined tool %s as live" % (rel, i + 1, tid))

# root README must tell the corrected story (must not contradict books.jsonl)
need("source-grounding-corrected" in readme,
     "root README.md does not tell the source-grounding-corrected Montgomery story")
need("v0.6-E Closure Review" in readme,
     "root README.md does not point to the v0.6-E Closure Review track")

# governance policy must list the actual quarantine set (must not contradict transition-memory)
pol = read("governance/state-coherence-policy.md") or ""
for tok in ("MNTII-006-A", "MNTII-006-B", "legacy"):
    need(tok in pol,
         "governance/state-coherence-policy.md current-quarantine does not name %s" % tok)
need("validated_intake" in pol,
     "governance/state-coherence-policy.md does not record the live E as validated_intake")

# compressed-prompt must hand off the CURRENT phase, not an old one
cp = read("transition-memory/compressed-prompt.md") or ""
need("v0.6" in cp,
     "transition-memory/compressed-prompt.md does not reflect the current v0.6 phase")
need(not re.search(r"التالي[^\n]{0,40}v0\.[0-5]\b", cp),
     "transition-memory/compressed-prompt.md points to an old v0.x phase as the next action")
need("v0.2 = Mileti" not in cp,
     "transition-memory/compressed-prompt.md still hands off to v0.2 Mileti (v0.1-era prompt)")

# quarantined treasure cards 001-015 must each carry a QUARANTINED status marker
tm_text = read(os.path.join(MONT, "treasure-map.md")) or ""
tm_lines = tm_text.splitlines()
for i, ln in enumerate(tm_lines):
    m = re.match(r"Treasure ID:\s*TREASURE-MNTII-(\d{3})\s*$", ln.strip())
    if m and 1 <= int(m.group(1)) <= 15:
        w = " ".join(tm_lines[i:i + 3]).lower()
        need("quarantin" in w,
             "treasure-map.md card TREASURE-MNTII-%s lacks a QUARANTINED status marker" % m.group(1))

# ---- STATE-REPAIR 006-D: single-source live state --------------------------------
# (a) Closed-unit stale-claim scan (repo-wide, NO superseded/closure exemptions):
#     once a unit is closure-reviewed PASS, no live line may describe it in present
#     tense as validated_intake / NOT closed / pending its review. Only past-lineage
#     phrasing ("entered as", Arabic equivalent) or an explicit "stale finding" note
#     is allowed. Historical audit reports (audits/) are pinned records and exempt.
CLOSURE_AUDITS = {"C": "v0.6-c-closure.md", "D": "v0.6-d-closure.md",
                  "E": "v0.6-e-closure.md", "F": "v0.6-f-closure.md",
                  "G": "v0.6-g-closure.md", "H": "v0.6-h-closure.md"}
closed_letters = []
for L, aud in CLOSURE_AUDITS.items():
    a = read(os.path.join("audits", aud))
    if a is not None and "PASS" in a:
        closed_letters.append(L)
for rel in story_files():
    if rel.startswith("audits/"):
        continue
    text = read(rel)
    if text is None:
        continue
    for i, ln in enumerate(text.splitlines()):
        # segment-scoped: a claim belongs to the unit mentioned before it, up to the
        # next unit mention on the same line (multi-unit summary lines stay precise).
        for mm in re.finditer(r"MNTII-006-([A-Z])(?![-A-Za-z])", ln):
            L = mm.group(1)
            if L not in closed_letters:
                continue
            rest = ln[mm.end():]
            nxt = re.search(r"MNTII-006-[A-Z]", rest)
            seg = rest[:nxt.start()] if nxt else rest
            seg_low = seg.lower()
            stale = ("validated_intake" in seg_low or "not closed" in seg_low
                     or ("pending v0.6-%s closure review" % L.lower()) in seg_low)
            if stale:
                exempt = ("entered as" in seg_low) or ("دخلت" in seg) or ("stale finding" in seg_low)
                need(exempt,
                     "%s:%d: describes CLOSED unit MNTII-006-%s as intake/NOT-closed/pending (stale live-state claim)"
                     % (rel, i + 1, L))
# (b) every closed unit's Status line must say CLOSED (uniform vocabulary)
for L in closed_letters:
    u = read(os.path.join(MONT, "units", "MNTII-006-%s.md" % L))
    if u is not None:
        need(re.search(r"\*\*Status:\*\*\s*CLOSED", u),
             "unit MNTII-006-%s is closure-reviewed PASS but its Status line is not CLOSED" % L)
# (c) unit files are historical records: their 'Next valid action' section must point
#     to the single live source, never define the live next action directly.
unit_globs = (glob.glob(os.path.join(ROOT, MONT, "units", "MNTII-006-*.md"))
              + glob.glob(os.path.join(ROOT, MONT, "units", "_quarantine", "*.md")))
for p in unit_globs:
    rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
    txt = read(rel) or ""
    m = re.search(r"## Next valid action\s*\n+((?:.*\n){1,5})", txt)
    if m:
        need("transition-memory/next-action.md" in m.group(1),
             "%s: 'Next valid action' does not point to transition-memory/next-action.md (live state must have one source)" % rel)
# (d) if F exists as intake, the live layers must not omit it from the Montgomery path
if f_txt is not None and not F_CLOSED:
    need(any(tok.startswith("F") for tok in trusted_tokens),
         "books.jsonl trusted_source_units omits the F intake while units/MNTII-006-F.md exists")
    need("TOOL-MONTGOMERY-PRIME-SUMS-TYPE-II-DIAGNOSTIC-001" in (caps or ""),
         "maps/current-capabilities.md omits the F-intake tool")
    need("MNTII-006-F" in (read(os.path.join(MONT, "missed-treasures.md")) or ""),
         "missed-treasures.md omits MNTII-006-F")
    need("v0.6-F Closure Review" in readme,
         "root README.md does not point to the v0.6-F Closure Review track")

# ---- STATE-REPAIR 006-E: chapter-status truth (chapter <-> unit map) --------------
# Coverage Audit 007 made chapter<->unit part of the truth. A live layer must never
# call a chapter 'unmined' while its unit exists, nor call Ch 18 mined/closed before
# a valid Ch-18 unit exists. 'unmined' is allowed only in historical/superseded/
# blocked-review contexts (audits/ and _quarantine/ are pinned records).
CHAPTER_UNITS = [("16", "MNTII-006-G.md"), ("17", "MNTII-006-F.md"),
                 ("18", "MNTII-006-H.md"),
                 ("19", "MNTII-006-C.md"), ("20", "MNTII-006-C.md"),
                 ("21", "MNTII-006-D.md"), ("22", "MNTII-006-E.md")]
mined_chapters = [ch for ch, u in CHAPTER_UNITS
                  if os.path.isfile(os.path.join(ROOT, MONT, "units", u))]
ch18_unit_exists = any(
    "Ch 18" in (read(os.path.relpath(p, ROOT).replace(os.sep, "/")) or "")
    for p in glob.glob(os.path.join(ROOT, MONT, "units", "MNTII-006-[H-Z].md")))
for rel in story_files():
    if rel.startswith("audits/") or "/_quarantine/" in rel:
        continue
    text = read(rel)
    if text is None:
        continue
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        low = ln.lower()
        # a mined chapter must not be called unmined in a live layer
        if ("unmined" in low) or ("غير مُعدَّن" in ln) or ("غير معدن" in ln):
            for ch in mined_chapters:
                if re.search(r"ch\s*%s\b" % ch, low) and not line_in_historical_context(lines, i):
                    need(False,
                         "%s:%d: calls mined chapter Ch %s 'unmined' while its unit exists" % (rel, i + 1, ch))
        # Ch 18 must not be called mined/closed before a valid Ch-18 unit exists
        if not ch18_unit_exists and re.search(r"ch\s*18\b[^\n]{0,60}\b(mined|closed)\b", low):
            if "unmined" not in low and not line_in_historical_context(lines, i):
                need(False,
                     "%s:%d: calls Ch 18 mined/closed before a valid Ch-18 unit exists" % (rel, i + 1))

# ---- STATE-REPAIR 006-F: executed-unit stale-denial + closed-count consistency ----
# STRICT exemption: these two checks accept ONLY a same-line historical marker.
# (The broad neighbourhood exemption tokens — especially 'legacy' — were demonstrated
#  to shield live defects whose lines merely mention the quarantined legacy-E.)
def line_marked_historical(ln):
    low = ln.lower()
    return ("historical" in low) or ("تاريخي" in ln)


# (a) Executed-unit stale-denial: a unit that EXISTS may never be described in a live
#     layer with denial phrases (not allowed / packet absent / permission not met /
#     not mined, or Arabic equivalents) unless the line itself is marked historical.
existing_letters = [L for L in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    if os.path.isfile(os.path.join(ROOT, MONT, "units", "MNTII-006-%s.md" % L))]
DENIAL_KEYS = ("not allowed", "packet absent", "permission not met",
               "the permission are not", "not mined", "غير مسموح", "لم يصدر إذن")
for rel in story_files():
    if rel.startswith("audits/") or "/_quarantine/" in rel:
        continue
    text = read(rel)
    if text is None:
        continue
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        low = ln.lower()
        for L in existing_letters:
            uid = "mntii-006-%s" % L.lower()
            if uid in low and (uid + "-legacy") not in low:
                if any((k in low) or (k in ln) for k in DENIAL_KEYS):
                    need(line_marked_historical(ln),
                         "%s:%d: describes EXECUTED unit MNTII-006-%s with a stale denial phrase"
                         % (rel, i + 1, L))
# (b) Closed-count consistency: textual counts of closed units in live layers must
#     match the actual number of closure-reviewed units.
WORD_NUM = {"three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
            "ثلاث": 3, "أربع": 4, "خمس": 5, "ست": 6, "سبع": 7, "ثمان": 8}
COUNT_PATTERNS = [
    re.compile(r"all (three|four|five|six|seven|eight) closure-reviewed", re.I),
    re.compile(r"(three|four|five|six|seven|eight) trusted units closed", re.I),
    re.compile(r"(ثلاث|أربع|خمس|ست|سبع|ثمان)[ُ]?\s+وحداتٍ\s+(?:موثوقةٍ\s+)?مُغلَقة"),
]
n_closed = len(closed_letters)
for rel in story_files():
    if rel.startswith("audits/") or "/_quarantine/" in rel:
        continue
    text = read(rel)
    if text is None:
        continue
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        for pat in COUNT_PATTERNS:
            m = pat.search(ln)
            if m and WORD_NUM.get(m.group(1).lower(), -1) != n_closed:
                need(line_marked_historical(ln),
                     "%s:%d: closed-unit count '%s' contradicts the actual closed count (%d)"
                     % (rel, i + 1, m.group(1), n_closed))

# ---- BOOK-OVERLAY CLOSURE truth (after AUDIT-CM-MONTGOMERY-OVERLAY-008) -----------
# Once the Montgomery overlay is closed, live layers must not contradict it, and the
# closure must never be read as mathematical closure.
if MONT_OVERLAY_CLOSED:
    # every PASS closure audit must still have its unit file (no chapter silently dropped
    # while an all-chapters claim stands)
    for L, aud in CLOSURE_AUDITS.items():
        a = read(os.path.join("audits", aud))
        if a is not None and "PASS" in a:
            need(os.path.isfile(os.path.join(ROOT, MONT, "units", "MNTII-006-%s.md" % L)),
                 "closure audit %s is PASS but units/MNTII-006-%s.md is missing" % (aud, L))
    NEG_TOKENS = ("not ", "no ", "never", "open", "unsolved", "uncrossed", "deferred",
                  "zero", "≠", "historical", "لا", "مفتوح", "تاريخي", "مؤجَّل")
    for rel in story_files():
        if rel.startswith("audits/") or "/_quarantine/" in rel:
            continue
        text = read(rel)
        if text is None:
            continue
        for i, ln in enumerate(text.splitlines()):
            low = ln.lower()
            mont_ctx = ("montgomery" in low or "mnt-ii" in low or "mntii" in low)
            # (1) no live partial-overlay claim about MONTGOMERY after its closure.
            #     Opera (v0.7) legitimately re-introduced partial_overlay as a live state for a
            #     different book; a line naming Opera attributes the partial_overlay there and is
            #     exempt — the Montgomery ban is what this check enforces.
            opera_ctx = ("opera" in low or "book-sieve-opera" in low or "opera-004" in low)
            if (mont_ctx and not opera_ctx
                    and ("partial_overlay" in low or "partial overlay" in low)):
                need(line_marked_historical(ln),
                     "%s:%d: live partial-overlay claim about Montgomery after book_overlay_closed" % (rel, i + 1))
            # (2) no live 'NOT book_overlay_closed' after closure
            if mont_ctx and ("not book_overlay" in low or "not book overlay" in low):
                need(line_marked_historical(ln),
                     "%s:%d: live NOT-book_overlay_closed claim after closure" % (rel, i + 1))
            # (3) no live 'Actually missing' item may coexist with the closed overlay
            if "actually missing" in low:
                need(line_marked_historical(ln) or ("zero" in low) or ("none" in low)
                     or ("فارغ" in ln),
                     "%s:%d: live 'Actually missing' item coexists with book_overlay_closed" % (rel, i + 1))
            # (4) overlay closure must never pair with Goldbach/RH/GRH/wall claims un-negated
            if "book_overlay_closed" in low and any(
                    k in low for k in ("goldbach", "rh ", "grh", "riemann", "wall")):
                need(any((n in low) or (n in ln) for n in NEG_TOKENS),
                     "%s:%d: book_overlay_closed paired with a Goldbach/RH/GRH/wall claim" % (rel, i + 1))

# ---- OPERA DE CRIBRO Opening Pass: scope-only guard (v0.7) --------------------
# Opera is opened scope-only: registered with a verified bibliographic identity, scope
# frozen, doctrine seeded — but NO mining, NO units, and NO trusted chapter classification
# before an authorized Treasure Packet. This guard protects that invariant.
OPERA = "ledgers/books/BOOK-SIEVE-OPERA-001"
opera_line = ""
for line in books.splitlines():
    if "BOOK-SIEVE-OPERA-001" in line:
        opera_line = line
if opera_line:
    try:
        opera_obj = json.loads(opera_line)
    except Exception:
        opera_obj = {}
    opera_status = opera_obj.get("status", "")
    opera_units = glob.glob(os.path.join(ROOT, OPERA, "OPERA-004-*.md"))
    if opera_units:
        # a real unit exists -> scope-only is over; status must have advanced past it
        need(opera_status not in ("available_not_imported", "scope_open"),
             "Opera unit file(s) exist but books.jsonl still says scope-only (mining left no status advance)")
        # OPERA-004-A state machine: packet-grounded intake -> closure (mirrors the Montgomery machines)
        a_txt = read(os.path.join(OPERA, "OPERA-004-A.md"))
        a_closure = read(os.path.join("audits", "v0.7-a-closure.md"))
        A_CLOSED = a_closure is not None and "PASS" in a_closure
        if a_closure is not None:
            need("PASS" in a_closure, "audits/v0.7-a-closure.md exists but does not record PASS")
        # OPERA-004-B state machine (packet-002 grounded intake -> closure)
        b_txt = read(os.path.join(OPERA, "OPERA-004-B.md"))
        b_closure = read(os.path.join("audits", "v0.7-b-closure.md"))
        B_CLOSED = b_closure is not None and "PASS" in b_closure
        if b_closure is not None:
            need("PASS" in b_closure, "audits/v0.7-b-closure.md exists but does not record PASS")
        # any un-closed unit keeps the book at partial_overlay (not scope_open, not book_overlay_closed)
        a_open = a_txt is not None and not A_CLOSED
        b_open = b_txt is not None and not B_CLOSED
        if a_open or b_open:
            need(opera_status == "partial_overlay",
                 "Opera has an un-closed unit but status is '%s' (should be partial_overlay)" % opera_status)
        # A state machine
        if a_txt is not None:
            need("Treasure Packet" in a_txt and "OPERA-TREASURE-PACKET-001" in a_txt,
                 "OPERA-004-A is not grounded in OPERA-TREASURE-PACKET-001")
            if A_CLOSED:
                need(re.search(r"\*\*Status:\*\*\s*CLOSED", a_txt),
                     "v0.7-a-closure PASS exists but OPERA-004-A is not marked Status: CLOSED")
            else:
                need(not re.search(r"\*\*Status:\*\*\s*CLOSED", a_txt),
                     "OPERA-004-A is marked Status: CLOSED but no v0.7-a-closure PASS exists")
                need(re.search(r"\*\*Status:\*\*[^\n]*validated_intake", a_txt),
                     "OPERA-004-A (intake) Status line is not validated_intake")
                need("not closed" in a_txt.lower(), "OPERA-004-A (intake) is not marked NOT closed")
            m = re.search(r"## Next valid action\s*\n+((?:.*\n){1,6})", a_txt)
            if m:
                need("transition-memory/next-action.md" in m.group(1),
                     "OPERA-004-A 'Next valid action' does not point to transition-memory/next-action.md")
        # B state machine
        if b_txt is not None:
            need("Treasure Packet" in b_txt and "OPERA-TREASURE-PACKET-002" in b_txt,
                 "OPERA-004-B is not grounded in OPERA-TREASURE-PACKET-002")
            if B_CLOSED:
                need(re.search(r"\*\*Status:\*\*\s*CLOSED", b_txt),
                     "v0.7-b-closure PASS exists but OPERA-004-B is not marked Status: CLOSED")
            else:
                need(not re.search(r"\*\*Status:\*\*\s*CLOSED", b_txt),
                     "OPERA-004-B is marked Status: CLOSED but no v0.7-b-closure PASS exists")
                need(re.search(r"\*\*Status:\*\*[^\n]*validated_intake", b_txt),
                     "OPERA-004-B (intake) Status line is not validated_intake")
                need("not closed" in b_txt.lower(), "OPERA-004-B (intake) is not marked NOT closed")
            m = re.search(r"## Next valid action\s*\n+((?:.*\n){1,6})", b_txt)
            if m:
                need("transition-memory/next-action.md" in m.group(1),
                     "OPERA-004-B 'Next valid action' does not point to transition-memory/next-action.md")
        # one unit per authorized packet: no OPERA-004-C before an explicit packet + permission
        need(not os.path.isfile(os.path.join(ROOT, OPERA, "OPERA-004-C.md")),
             "OPERA-004-C exists; no further Opera unit is allowed without a packet and permission")
    else:
        # scope-only: status must be exactly scope_open (never mined / partial / closed)
        need(opera_status == "scope_open",
             "Opera has no units yet but books.jsonl status is '%s' (Opening Pass must stay scope_open)"
             % opera_status)
        for doc in ("v0.7-scope.md", "v0.7-scope-freeze.md"):
            need(os.path.isfile(os.path.join(ROOT, OPERA, doc)),
                 "Opera scope_open but %s is missing" % doc)
        for ov in ("treasure-map.md", "normalization-ledger.md",
                   "integration-links.md", "missed-treasures.md"):
            ovt = read(os.path.join(OPERA, ov))
            need(ovt is not None, "Opera overlay %s is missing" % ov)
            if ovt is not None:
                low = ovt.lower()
                need("scope-only" in low or "no treasures extracted" in low,
                     "Opera overlay %s is not marked scope-only / empty" % ov)
        need(os.path.isfile(os.path.join(ROOT, "governance",
             "scope-amendment-and-debt-policy.md")),
             "Opera opened but governance/scope-amendment-and-debt-policy.md is missing")
        need("Opera" in nexta and "Packet" in nexta,
             "next-action.md does not reflect the Opera scope-only wait (awaiting the first packet)")

if issues:
    print("FAIL - %d state-coherence issue(s):" % len(issues))
    for i in issues:
        print("  [coherence]", i)
    sys.exit(1)
print("PASS - state coherence: repository state files are consistent (repository-truth check, repo-wide sweep).")
sys.exit(0)
