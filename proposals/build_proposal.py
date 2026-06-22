#!/usr/bin/env python3
"""Generate a professional PDF concept note / proposal for the three
replication experiments discussed with Julie Combs.

Output: proposals/Three_Experiments_Concept_Note.pdf
"""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    NextPageTemplate,
    PageBreak,
    HRFlowable,
)

# ---------------------------------------------------------------------------
# Palette
# ---------------------------------------------------------------------------
NAVY = colors.HexColor("#16263F")
ACCENT = colors.HexColor("#1F6F8B")
LIGHT = colors.HexColor("#E8EEF2")
GREY = colors.HexColor("#5A6470")
RULE = colors.HexColor("#C9D4DC")

OUTPUT = "/home/user/dmtx-ecuador/proposals/Three_Experiments_Concept_Note.pdf"

# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
styles = getSampleStyleSheet()


def S(name, **kw):
    return ParagraphStyle(name, **kw)


title_style = S("Title2", fontName="Helvetica-Bold", fontSize=26, leading=30,
                textColor=NAVY, alignment=TA_LEFT)
subtitle_style = S("Subtitle2", fontName="Helvetica", fontSize=13, leading=18,
                   textColor=ACCENT, alignment=TA_LEFT)
meta_style = S("Meta", fontName="Helvetica", fontSize=9.5, leading=14,
               textColor=GREY)
h1 = S("H1", fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=NAVY,
       spaceBefore=16, spaceAfter=6)
h2 = S("H2", fontName="Helvetica-Bold", fontSize=11.5, leading=15, textColor=ACCENT,
       spaceBefore=10, spaceAfter=3)
body = S("Body", fontName="Helvetica", fontSize=10, leading=15, textColor=colors.HexColor("#22272E"),
         alignment=TA_JUSTIFY, spaceAfter=6)
bullet = S("Bullet", fontName="Helvetica", fontSize=10, leading=14,
           textColor=colors.HexColor("#22272E"), leftIndent=14, bulletIndent=4, spaceAfter=2)
small = S("Small", fontName="Helvetica", fontSize=8.5, leading=12, textColor=GREY)
link = S("Link", fontName="Helvetica", fontSize=9, leading=13, textColor=ACCENT,
         leftIndent=14, spaceAfter=1)
tablecell = S("Cell", fontName="Helvetica", fontSize=9, leading=12,
              textColor=colors.HexColor("#22272E"))
tablecellb = S("CellB", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=NAVY)
tablehead = S("CellH", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=colors.white)

# ---------------------------------------------------------------------------
# Page furniture
# ---------------------------------------------------------------------------
PROJECT = "Replication Studies in Consciousness &amp; Altered States"


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(0.9 * inch, 0.7 * inch, 7.6 * inch, 0.7 * inch)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)
    canvas.drawString(0.9 * inch, 0.52 * inch, "Concept Note  ·  Prepared by Ney Torres")
    canvas.drawRightString(7.6 * inch, 0.52 * inch, "Page %d" % doc.page)
    canvas.drawCentredString(4.25 * inch, 0.52 * inch, "Confidential draft for discussion")
    canvas.restoreState()


def cover(canvas, doc):
    canvas.saveState()
    # top band
    canvas.setFillColor(NAVY)
    canvas.rect(0, 9.0 * inch, LETTER[0], 2.0 * inch, fill=1, stroke=0)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, 8.93 * inch, LETTER[0], 0.07 * inch, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(0.9 * inch, 10.35 * inch, "RESEARCH CONCEPT NOTE")
    canvas.setFont("Helvetica", 10)
    canvas.drawString(0.9 * inch, 10.12 * inch, "Three Candidate Experiments for University Replication")
    canvas.restoreState()
    footer(canvas, doc)


# Document with two page templates: cover + content
doc = BaseDocTemplate(
    OUTPUT, pagesize=LETTER,
    leftMargin=0.9 * inch, rightMargin=0.9 * inch,
    topMargin=0.95 * inch, bottomMargin=0.9 * inch,
    title="Three Experiments — Research Concept Note",
    author="Ney Torres",
)
content_frame = Frame(0.9 * inch, 0.85 * inch, LETTER[0] - 1.8 * inch,
                      LETTER[1] - 1.8 * inch, id="content")
cover_frame = Frame(0.9 * inch, 0.85 * inch, LETTER[0] - 1.8 * inch,
                    7.7 * inch, id="cover")
doc.addPageTemplates([
    PageTemplate(id="Cover", frames=[cover_frame], onPage=cover),
    PageTemplate(id="Content", frames=[content_frame], onPage=footer),
])

story = []

# ---------------------------------------------------------------------------
# COVER
# ---------------------------------------------------------------------------
story.append(Spacer(1, 0.35 * inch))
story.append(Paragraph("Three Experiments for Rigorous<br/>University Replication", title_style))
story.append(Spacer(1, 0.1 * inch))
story.append(Paragraph("A concept note on testing extraordinary claims about consciousness "
                       "under clean, ethical, preregistered, and publishable conditions.",
                       subtitle_style))
story.append(Spacer(1, 0.35 * inch))
story.append(HRFlowable(width="100%", thickness=1, color=RULE))
story.append(Spacer(1, 0.18 * inch))

meta_tbl = Table([
    [Paragraph("<b>Prepared for</b>", meta_style), Paragraph("Julie Combs", meta_style)],
    [Paragraph("<b>Prepared by</b>", meta_style), Paragraph("Ney Torres", meta_style)],
    [Paragraph("<b>Date</b>", meta_style), Paragraph("22 June 2026", meta_style)],
    [Paragraph("<b>Purpose</b>", meta_style),
     Paragraph("Rough proposals and indicative budgets to support early "
               "conversations with university partners.", meta_style)],
    [Paragraph("<b>Status</b>", meta_style),
     Paragraph("Draft for discussion — figures are order-of-magnitude estimates.", meta_style)],
], colWidths=[1.3 * inch, 4.5 * inch])
meta_tbl.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LINEBELOW", (0, 0), (-1, -2), 0.4, LIGHT),
]))
story.append(meta_tbl)
story.append(Spacer(1, 0.25 * inch))
story.append(Paragraph(
    "<b>Framing.</b> All three studies are designed as <i>replication / falsification</i> "
    "studies. The aim is not to prove extraordinary claims, but to test them under conditions "
    "that are publishable even when the result is negative. A clean null result is a valuable "
    "scientific contribution; a positive result would be highly significant.", body))
story.append(Spacer(1, 0.08 * inch))
story.append(Paragraph(
    "<b>Costing basis.</b> Budgets are grounded in <b>Cuenca, Ecuador</b> conditions: local "
    "academic and clinical salaries, and the assumption that major equipment (EEG, fMRI, infusion "
    "pumps, monitoring) is <b>borrowed from partner institutions rather than purchased</b>. "
    "Equipment lines therefore cover access, transport, calibration, and consumables only. All "
    "figures are in USD (Ecuador's currency).", body))

story.append(NextPageTemplate("Content"))
story.append(PageBreak())

# ---------------------------------------------------------------------------
# EXECUTIVE SUMMARY
# ---------------------------------------------------------------------------
story.append(Paragraph("Executive Summary", h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "This note outlines three candidate experiments that could anchor a university research "
    "agenda on altered states of consciousness, neurophenomenology, and the scientific study of "
    "extraordinary human experience. Each is summarised below with a core idea, a proposed design, "
    "required infrastructure, ethical considerations, and an indicative budget. A comparative "
    "budget table and a longer pipeline of ten further candidates are included at the end.", body))

summary_rows = [
    [Paragraph("Study", tablehead), Paragraph("Core question", tablehead),
     Paragraph("Indicative budget", tablehead), Paragraph("Risk / complexity", tablehead)],
    [Paragraph("<b>1. Extended-State DMT (DMTx)</b>", tablecellb),
     Paragraph("Can the DMT state be safely extended and characterised in real time?", tablecell),
     Paragraph("$90k – $150k", tablecell),
     Paragraph("High — controlled substance, medical", tablecell)],
    [Paragraph("<b>2. Brain-to-Brain Correlation</b>", tablecellb),
     Paragraph("Do separated, paired subjects show correlated EEG responses?", tablecell),
     Paragraph("$35k – $55k", tablecell),
     Paragraph("Medium — design rigor is everything", tablecell)],
    [Paragraph("<b>3. Trance / Healer Neurophysiology</b>", tablecellb),
     Paragraph("Do practitioners enter a reproducible, distinct brain state?", tablecell),
     Paragraph("$30k – $50k", tablecell),
     Paragraph("Low–Medium — recruitment-limited", tablecell)],
]
st = Table(summary_rows, colWidths=[1.55 * inch, 2.5 * inch, 1.15 * inch, 1.5 * inch])
st.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING", (0, 0), (-1, -1), 7),
    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("GRID", (0, 0), (-1, -1), 0.4, RULE),
]))
story.append(Spacer(1, 0.05 * inch))
story.append(st)
story.append(Spacer(1, 0.12 * inch))
story.append(Paragraph(
    "<b>Recommended sequencing.</b> Studies 2 and 3 are lower-cost, lower-risk, and faster to "
    "ethics approval; either could serve as a credible first project that demonstrates rigor to "
    "partners and funders. Study 1 (DMTx) is the scientific flagship but carries the heaviest "
    "regulatory, medical, and budgetary load and is best pursued once institutional relationships "
    "and a clinical partner are in place.", body))


# ---------------------------------------------------------------------------
# Helper for a full proposal block
# ---------------------------------------------------------------------------
def proposal(number, title, idea_html, design_items, equipment, ethics, timeline,
             budget_rows, budget_total, references):
    story.append(PageBreak())
    # header band
    band = Table([[Paragraph(f'<font color="white"><b>EXPERIMENT {number}</b></font>', small)]],
                 colWidths=[6.7 * inch])
    band.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(band)
    story.append(Spacer(1, 4))
    story.append(Paragraph(title, h1))
    story.append(HRFlowable(width="100%", thickness=1, color=RULE, spaceAfter=6))

    story.append(Paragraph("Core idea", h2))
    story.append(Paragraph(idea_html, body))

    story.append(Paragraph("Proposed design", h2))
    for it in design_items:
        story.append(Paragraph(f"•&nbsp;&nbsp;{it}", bullet))
    story.append(Spacer(1, 4))

    # two-column equipment + ethics
    eq_html = "<b>Key infrastructure &amp; equipment</b><br/>" + "<br/>".join(f"• {e}" for e in equipment)
    et_html = "<b>Ethical &amp; safety considerations</b><br/>" + "<br/>".join(f"• {e}" for e in ethics)
    two = Table([[Paragraph(eq_html, S("eq", fontName="Helvetica", fontSize=9, leading=13,
                                       textColor=colors.HexColor("#22272E"))),
                  Paragraph(et_html, S("et", fontName="Helvetica", fontSize=9, leading=13,
                                       textColor=colors.HexColor("#22272E")))]],
                colWidths=[3.35 * inch, 3.35 * inch])
    two.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (0, 0), LIGHT),
        ("BACKGROUND", (1, 0), (1, 0), colors.HexColor("#F3ECE6")),
        ("BOX", (0, 0), (0, 0), 0.5, RULE),
        ("BOX", (1, 0), (1, 0), 0.5, colors.HexColor("#E3D5C8")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(two)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Indicative timeline", h2))
    story.append(Paragraph(timeline, body))

    story.append(Paragraph("Indicative budget (rough / general)", h2))
    rows = [[Paragraph("Cost category", tablehead), Paragraph("Estimate (USD)", tablehead)]]
    for cat, amt in budget_rows:
        rows.append([Paragraph(cat, tablecell), Paragraph(amt, tablecell)])
    rows.append([Paragraph("<b>Indicative total</b>", tablecellb),
                 Paragraph(f"<b>{budget_total}</b>", tablecellb)])
    bt = Table(rows, colWidths=[4.9 * inch, 1.8 * inch])
    bt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [colors.white, LIGHT]),
        ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#D8E4EA")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
    ]))
    story.append(bt)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Key references &amp; links", h2))
    for r in references:
        story.append(Paragraph(f'•&nbsp;<link href="{r[1]}" color="#1F6F8B">{r[0]}</link>', link))


# ---------------------------------------------------------------------------
# EXPERIMENT 1
# ---------------------------------------------------------------------------
proposal(
    1,
    "Extended-State DMT / DMTx",
    "Rather than studying DMT as a very short (5–15 minute) experience, this protocol uses a "
    "controlled intravenous loading dose followed by a target-controlled maintenance infusion to "
    "<b>extend and stabilise the DMT state</b> for an experimentally useful window. This makes it "
    "possible to study the phenomenology, neural correlates, and any recurring structures of the "
    "experience while collecting real-time physiological and neuroimaging data. The informal "
    "DMT / laser-perception idea we discussed would sit inside this framework as a small, blinded "
    "perceptual sub-study rather than as the flagship aim.",
    [
        "<b>Design:</b> open-label pharmacokinetic / pharmacodynamic pilot, n ≈ 8–12 healthy, "
        "psychedelic-experienced volunteers, within-subject dose escalation.",
        "<b>Primary outcomes:</b> safety and tolerability of extended infusion; feasibility of "
        "maintaining a stable subjective state at a target plasma level.",
        "<b>Secondary outcomes:</b> EEG signatures (spectral power, complexity / entropy, "
        "connectivity); validated phenomenology scales; structured post-session interviews.",
        "<b>Optional blinded sub-study:</b> randomised, blinded perceptual tasks delivered during "
        "the stable state to test specific claims under controlled conditions.",
        "<b>Analysis:</b> preregistered, with predefined safety stopping rules and primary endpoints.",
    ],
    [
        "Clinical research unit with anaesthesia-grade monitoring (partner hospital)",
        "Target-controlled IV infusion pump(s) — borrowed",
        "Research-grade EEG &amp; physiological monitoring — borrowed",
        "Pharmaceutical-grade DMT and hospital pharmacy handling",
        "Controlled-substance storage and chain-of-custody",
    ],
    [
        "Schedule I / controlled-substance licensing and import permits",
        "Full IRB / research-ethics board review",
        "On-site physician and resuscitation capability",
        "Rigorous screening; cardiac and psychiatric exclusions",
        "Trained psychological support and integration",
    ],
    "Approximately 18–24 months: 6–9 months for regulatory, ethics, and drug supply; "
    "3 months setup and staff training; 6–9 months data collection; 3–6 months analysis and write-up.",
    [
        ("Regulatory, ethics &amp; controlled-substance permits (Ecuador)", "$8,000"),
        ("Pharmaceutical-grade DMT supply &amp; secure handling", "$20,000"),
        ("Clinical &amp; medical staff (physician, anaesthesia, nurse, psychiatrist) — local rates", "$25,000"),
        ("Borrowed EEG / monitoring — access, transport, calibration &amp; consumables", "$8,000"),
        ("Core research personnel (PI, postdoc, RAs, analyst — ~1 yr, Cuenca rates)", "$40,000"),
        ("Participant screening, compensation &amp; facility", "$8,000"),
        ("Data analysis, computing, dissemination &amp; contingency", "$6,000"),
    ],
    "≈ $90,000 – $150,000",
    [
        ("Gallimore &amp; Strassman (2016), Frontiers in Pharmacology",
         "https://doi.org/10.3389/fphar.2016.00211"),
        ("Extended DMT study (PMC10851633)",
         "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10851633/"),
        ("Continuous DMT infusion study (PMC12032411)",
         "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12032411/"),
    ],
)

# ---------------------------------------------------------------------------
# EXPERIMENT 2
# ---------------------------------------------------------------------------
proposal(
    2,
    "Brain-to-Brain Correlation / &ldquo;Transferred Potential&rdquo; Replication",
    "Inspired by Jacobo Grinberg&rsquo;s controversial work on &ldquo;transferred potentials,&rdquo; "
    "in which two people are placed in separate rooms, one receives a stimulus, and the other&rsquo;s "
    "brain activity is monitored for correlated responses. The claim is extraordinary — which is "
    "exactly why it deserves a <b>modern, rigorously controlled replication</b>. The scientific value "
    "here lies almost entirely in design quality: double-blinding, shielding, randomised timing, and "
    "fully automated, preregistered analysis remove the loopholes that made the original work "
    "impossible to interpret.",
    [
        "<b>Design:</b> paired-subject EEG study, ≈ 25–30 pairs (emotionally bonded and stranger "
        "pairs), &ldquo;sender&rdquo; and &ldquo;receiver&rdquo; in separate electromagnetically "
        "shielded rooms.",
        "<b>Stimulus:</b> randomised, computer-triggered sensory stimuli to the sender at times "
        "unknown to the receiver and to all experimenters present.",
        "<b>Primary outcome:</b> preregistered test for time-locked correlated activity in the "
        "receiver&rsquo;s EEG during sender-stimulation vs. matched null windows.",
        "<b>Controls:</b> sham/no-sender blocks, sensor-level artifact rejection, and analyst "
        "blinding to condition labels.",
        "<b>Statistics:</b> preregistered effect-size threshold, Bayesian + frequentist criteria; a "
        "well-powered null is a publishable outcome.",
    ],
    [
        "Two research-grade EEG systems, time-synchronised — borrowed",
        "Electromagnetically shielded / Faraday-isolated rooms (existing facility)",
        "Hardware trigger &amp; precision timing infrastructure",
        "Automated, preregistered analysis pipeline",
        "Audio/RF isolation verification",
    ],
    [
        "IRB / ethics approval (low physical risk)",
        "Informed consent; right to withdraw",
        "Pre-registration on OSF / AsPredicted before data collection",
        "Independent verification of room isolation",
        "Open data and analysis code for full transparency",
    ],
    "Approximately 12–15 months: 2–3 months ethics and preregistration; 2 months setup and "
    "isolation testing; 5–6 months paired data collection; 3–4 months analysis and write-up.",
    [
        ("Borrowed EEG — transport, caps/electrodes, gel, calibration", "$4,000"),
        ("Shielded-room setup &amp; isolation testing (existing facility)", "$5,000"),
        ("Core personnel (PI part-time, postdoc, 2 RAs, analyst — ~1 yr, Cuenca rates)", "$30,000"),
        ("Participant recruitment &amp; compensation (~60 participants)", "$4,000"),
        ("Preregistration, replication design &amp; statistical consulting", "$3,000"),
        ("Computing, open-data hosting &amp; dissemination", "$2,000"),
    ],
    "≈ $35,000 – $55,000",
    [
        ("Jacobo Grinberg — background &amp; publication reference (Wikipedia, ES)",
         "https://es.wikipedia.org/wiki/Jacobo_Grinberg"),
        ("Related separated-subject EEG study (PubMed 12972348)",
         "https://pubmed.ncbi.nlm.nih.gov/12972348/"),
    ],
)

# ---------------------------------------------------------------------------
# EXPERIMENT 3
# ---------------------------------------------------------------------------
proposal(
    3,
    "Shamans / Healers / Trance Practitioners under EEG or fMRI",
    "Study shamans, healers, meditators, or trance practitioners while they enter their claimed "
    "healing or altered state, and compare their brain activity and physiology against matched "
    "controls and against their own ordinary rest, imagination, and meditation. Crucially, this "
    "study does <b>not</b> need to begin by claiming that &ldquo;healing energy&rdquo; is real. The "
    "first, stronger scientific question is simply: <i>do trained practitioners enter a reproducible "
    "neurophysiological state that is measurably different from ordinary baselines?</i> If yes, a "
    "later phase can test whether that state has any measurable effect on recipients.",
    [
        "<b>Design:</b> within-subject, multi-condition comparison (trance vs. rest vs. imagery vs. "
        "meditation), ≈ 15–25 experienced practitioners + matched controls.",
        "<b>Primary outcome:</b> reproducible, practitioner-specific EEG/fMRI signature that "
        "discriminates the trance state from control conditions above chance.",
        "<b>Secondary outcomes:</b> autonomic measures (HRV, electrodermal activity, respiration); "
        "state classification with cross-validated machine learning.",
        "<b>Phase 2 (optional):</b> blinded recipient study testing for any physiological or "
        "perceptual effect on a second person.",
        "<b>Analysis:</b> preregistered classification accuracy and effect-size thresholds.",
    ],
    [
        "Research-grade EEG and/or fMRI scanner access — borrowed",
        "Autonomic / peripheral physiology recording (HRV, EDA) — borrowed",
        "Synchronised audio-video for state annotation",
        "Analysis workstation &amp; ML pipeline",
        "Quiet, controlled recording environment",
    ],
    [
        "IRB / ethics approval; culturally respectful protocol",
        "Community consultation &amp; fair compensation for practitioners",
        "Informed consent honouring practitioners&rsquo; traditions",
        "Clear non-medical-claim framing in all materials",
        "Pre-registration of hypotheses and analysis",
    ],
    "Approximately 12–18 months: 2–3 months ethics, community engagement, and recruitment; "
    "5–7 months data collection (recruitment-paced); 3–5 months analysis and write-up.",
    [
        ("Borrowed EEG / fMRI — scanner access fees &amp; consumables (~40 sessions)", "$5,000"),
        ("Core personnel (postdoc, RAs, data analyst — ~1 yr, Cuenca rates)", "$28,000"),
        ("Practitioner recruitment, travel &amp; compensation", "$6,000"),
        ("Peripheral physiology (HRV, EDA) — borrowed / low-cost", "$2,000"),
        ("Ethics, preregistration, dissemination &amp; contingency", "$3,000"),
    ],
    "≈ $30,000 – $50,000",
    [
        ("Cognitive / shamanic-style trance research (arXiv 2509.19254)",
         "https://arxiv.org/abs/2509.19254"),
        ("Trance &amp; neurophysiology — general background (Wikipedia)",
         "https://en.wikipedia.org/wiki/Trance"),
    ],
)

# ---------------------------------------------------------------------------
# COMPARATIVE BUDGET + NOTES
# ---------------------------------------------------------------------------
story.append(PageBreak())
story.append(Paragraph("Comparative Budget Overview", h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "The figures below are <b>rough, order-of-magnitude estimates</b> for pilot studies run in "
    "<b>Cuenca, Ecuador</b>, using <b>local salaries</b> and <b>borrowed equipment</b> from partner "
    "institutions (no major hardware purchases). They are deliberately lean; the largest variable "
    "is personnel time. If a study required buying its own EEG/MRI hardware or a dedicated shielded "
    "facility, costs would rise substantially — but that is explicitly not assumed here.", body))

comp = [
    [Paragraph("Study", tablehead), Paragraph("Low", tablehead),
     Paragraph("High", tablehead), Paragraph("Typical duration", tablehead),
     Paragraph("First-mover?", tablehead)],
    [Paragraph("1 · Extended-State DMT (DMTx)", tablecellb), Paragraph("$90k", tablecell),
     Paragraph("$150k", tablecell), Paragraph("18–24 months", tablecell),
     Paragraph("Flagship — later phase", tablecell)],
    [Paragraph("2 · Brain-to-Brain Correlation", tablecellb), Paragraph("$35k", tablecell),
     Paragraph("$55k", tablecell), Paragraph("12–15 months", tablecell),
     Paragraph("Strong candidate", tablecell)],
    [Paragraph("3 · Trance / Healer Neurophysiology", tablecellb), Paragraph("$30k", tablecell),
     Paragraph("$50k", tablecell), Paragraph("12–18 months", tablecell),
     Paragraph("Strong candidate", tablecell)],
    [Paragraph("<b>Combined programme (all three)</b>", tablecellb),
     Paragraph("<b>$155k</b>", tablecellb), Paragraph("<b>$255k</b>", tablecellb),
     Paragraph("~2–3 years phased", tablecell), Paragraph("—", tablecell)],
]
ct = Table(comp, colWidths=[2.5 * inch, 0.85 * inch, 0.85 * inch, 1.3 * inch, 1.2 * inch])
ct.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("ROWBACKGROUNDS", (0, 1), (-1, -2), [colors.white, LIGHT]),
    ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#D8E4EA")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ALIGN", (1, 0), (2, -1), "RIGHT"),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING", (0, 0), (-1, -1), 7),
    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("GRID", (0, 0), (-1, -1), 0.4, RULE),
]))
story.append(Spacer(1, 4))
story.append(ct)
story.append(Spacer(1, 6))
story.append(Paragraph(
    "All totals assume borrowed equipment and Cuenca-based personnel. Studies 2 and 3 are modest "
    "enough to run as graduate / faculty research projects; Study 1 (DMTx) carries the clinical, "
    "drug, and regulatory load that keeps it the most expensive even at local prices.", small))

story.append(Paragraph("Cross-Cutting Principles", h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=8))
for t, d in [
    ("Replication, not advocacy",
     "Every study is framed to be publishable whether the result is positive or null. We are "
     "testing claims, not defending them."),
    ("Preregistration by default",
     "Hypotheses, sample sizes, and analysis plans are registered before data collection on OSF or "
     "a comparable platform, protecting against bias and post-hoc storytelling."),
    ("Ethics first",
     "Each study is designed to be ethically approvable at a mainstream university, with appropriate "
     "review, consent, safety, and (for Study 3) cultural respect."),
    ("Open and transparent",
     "Open data and analysis code wherever ethically possible, so results can be independently "
     "verified — the single most important safeguard for controversial questions."),
]:
    story.append(Paragraph(f"<b>{t}.</b> {d}", body))

# Broader pipeline
story.append(Paragraph("Broader Pipeline — Ten Further Candidates", h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "Beyond the three priority studies, the following are strong additional replication candidates "
    "in consciousness and altered-states research, available to build out a longer programme:", body))
pipeline = [
    "Real-time communication with lucid dreamers during REM sleep",
    "Psilocybin and increased brain-state repertoire",
    "Ayahuasca and brain entropy / network reorganization",
    "Expert meditators and high-amplitude gamma synchrony",
    "Hypnosis and changes in pain, agency, and self-perception",
    "Breathwork-induced non-ordinary states without psychedelics",
    "Ganzfeld / sensory deprivation and internally generated perception",
    "Near-death experience research and end-of-life brain activity",
    "Anesthesia and perturbational complexity as a measure of consciousness",
    "Virtual-reality body-transfer or out-of-body illusion experiments",
]
left = pipeline[:5]
right = pipeline[5:]
pl = Table([[
    Paragraph("<br/>".join(f"{i+1}. {x}" for i, x in enumerate(left)),
              S("pl", fontName="Helvetica", fontSize=9.5, leading=16, textColor=colors.HexColor("#22272E"))),
    Paragraph("<br/>".join(f"{i+6}. {x}" for i, x in enumerate(right)),
              S("pr", fontName="Helvetica", fontSize=9.5, leading=16, textColor=colors.HexColor("#22272E"))),
]], colWidths=[3.35 * inch, 3.35 * inch])
pl.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
story.append(pl)
story.append(Spacer(1, 0.2 * inch))
story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
story.append(Paragraph(
    "Prepared by Ney Torres · 22 June 2026 · Draft concept note for discussion with university "
    "partners. All budget figures are indicative and subject to refinement with a host institution.",
    small))

doc.build(story)
print("WROTE", OUTPUT)
