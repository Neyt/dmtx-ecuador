# Three Experiments — Research Concept Note

Prepared in response to Julie Combs' request (email "3 experiments", 22 June 2026)
for rough proposals and general budgets to share with university partners.

## Contents

- **`Three_Experiments_Concept_Note.pdf`** — formatted concept note (cover page,
  per-experiment proposals, comparative budget table, references). This is the
  document to attach when replying to Julie.
- **`build_proposal.py`** — ReportLab script that generates the PDF.

## The three priority studies

| # | Study | Core question | Indicative budget | Duration |
|---|-------|---------------|-------------------|----------|
| 1 | Extended-State DMT (DMTx) | Can the DMT state be safely extended and characterised in real time? | $450k – $650k | 18–24 mo |
| 2 | Brain-to-Brain Correlation ("transferred potential" replication) | Do separated, paired subjects show correlated EEG responses? | $250k – $350k | 12–15 mo |
| 3 | Trance / Healer Neurophysiology | Do practitioners enter a reproducible, distinct brain state? | $200k – $320k | 12–18 mo |

All three are framed as replication / falsification studies: preregistered,
ethically approvable, and publishable even when the result is negative.

## Rebuild the PDF

```bash
pip install reportlab
python3 proposals/build_proposal.py
```
