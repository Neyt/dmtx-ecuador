#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la nota conceptual / propuesta en PDF (español) para los tres
experimentos de replicación conversados con Julie Combs.

Salida: proposals/Tres_Experimentos_Nota_Conceptual.pdf
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
# Paleta
# ---------------------------------------------------------------------------
NAVY = colors.HexColor("#16263F")
ACCENT = colors.HexColor("#1F6F8B")
LIGHT = colors.HexColor("#E8EEF2")
GREY = colors.HexColor("#5A6470")
RULE = colors.HexColor("#C9D4DC")

OUTPUT = "/home/user/dmtx-ecuador/proposals/Tres_Experimentos_Nota_Conceptual.pdf"

# ---------------------------------------------------------------------------
# Estilos
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
# Elementos de página
# ---------------------------------------------------------------------------
def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(0.9 * inch, 0.7 * inch, 7.6 * inch, 0.7 * inch)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)
    canvas.drawString(0.9 * inch, 0.52 * inch, "Nota conceptual  ·  Preparada por Ney Torres")
    canvas.drawRightString(7.6 * inch, 0.52 * inch, "Página %d" % doc.page)
    canvas.drawCentredString(4.25 * inch, 0.52 * inch, "Borrador confidencial para discusión")
    canvas.restoreState()


def cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 9.0 * inch, LETTER[0], 2.0 * inch, fill=1, stroke=0)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, 8.93 * inch, LETTER[0], 0.07 * inch, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(0.9 * inch, 10.35 * inch, "NOTA CONCEPTUAL DE INVESTIGACIÓN")
    canvas.setFont("Helvetica", 10)
    canvas.drawString(0.9 * inch, 10.12 * inch, "Tres experimentos candidatos para la Universidad de Cuenca")
    canvas.restoreState()
    footer(canvas, doc)


doc = BaseDocTemplate(
    OUTPUT, pagesize=LETTER,
    leftMargin=0.9 * inch, rightMargin=0.9 * inch,
    topMargin=0.95 * inch, bottomMargin=0.9 * inch,
    title="Tres experimentos — Nota conceptual de investigación",
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
# PORTADA
# ---------------------------------------------------------------------------
story.append(Spacer(1, 0.35 * inch))
story.append(Paragraph("Tres experimentos para la<br/>Universidad de Cuenca", title_style))
story.append(Spacer(1, 0.1 * inch))
story.append(Paragraph("Una nota conceptual sobre estudios de replicación rigurosos, éticos y "
                       "liderados por la universidad acerca de la consciencia y los estados "
                       "alterados — propuestos en alineación con la misión y la visión de la "
                       "Universidad.", subtitle_style))
story.append(Spacer(1, 0.35 * inch))
story.append(HRFlowable(width="100%", thickness=1, color=RULE))
story.append(Spacer(1, 0.18 * inch))

meta_tbl = Table([
    [Paragraph("<b>Institución</b>", meta_style),
     Paragraph("Universidad de Cuenca · Cuenca, Ecuador", meta_style)],
    [Paragraph("<b>Preparada para</b>", meta_style), Paragraph("Julie Combs", meta_style)],
    [Paragraph("<b>Preparada por</b>", meta_style), Paragraph("Ney Torres", meta_style)],
    [Paragraph("<b>Fecha</b>", meta_style), Paragraph("23 de junio de 2026", meta_style)],
    [Paragraph("<b>Propósito</b>", meta_style),
     Paragraph("Propuestas preliminares y presupuestos indicativos para apoyar las primeras "
               "conversaciones con socios universitarios.", meta_style)],
    [Paragraph("<b>Estado</b>", meta_style),
     Paragraph("Borrador para discusión — las cifras son estimaciones de orden de magnitud.", meta_style)],
], colWidths=[1.4 * inch, 4.4 * inch])
meta_tbl.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LINEBELOW", (0, 0), (-1, -2), 0.4, LIGHT),
]))
story.append(meta_tbl)
story.append(Spacer(1, 0.25 * inch))
story.append(Paragraph(
    "<b>Enfoque.</b> Los tres estudios están diseñados como estudios de "
    "<i>replicación / falsación</i>. El objetivo no es demostrar afirmaciones extraordinarias, "
    "sino ponerlas a prueba bajo condiciones que sean publicables incluso cuando el resultado sea "
    "negativo. Un resultado nulo y limpio es una contribución científica valiosa; un resultado "
    "positivo sería de gran relevancia.", body))
story.append(Spacer(1, 0.08 * inch))
story.append(Paragraph(
    "<b>Base de costos.</b> Los presupuestos están basados en las condiciones de "
    "<b>Cuenca, Ecuador</b>: salarios académicos y clínicos locales, y el supuesto de que el "
    "equipamiento principal (EEG, fMRI, bombas de infusión, monitoreo) se "
    "<b>toma prestado de instituciones aliadas en lugar de comprarse</b>. Por lo tanto, las líneas "
    "de equipamiento cubren únicamente acceso, transporte, calibración e insumos. Todas las cifras "
    "están en USD (la moneda de Ecuador). Cada estudio se presenta como un rango — un límite "
    "inferior <b>apalancado por alianzas</b> y un límite superior con <b>costos completos</b> "
    "(explicado en la página de presupuesto comparativo).", body))

story.append(NextPageTemplate("Content"))
story.append(PageBreak())

# ---------------------------------------------------------------------------
# ALINEACIÓN CON LA UNIVERSIDAD DE CUENCA
# ---------------------------------------------------------------------------
story.append(Paragraph("Alineación con la Universidad de Cuenca", h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "Esta agenda de investigación se propone específicamente para la <b>Universidad de Cuenca</b>. "
    "Está diseñada no solo para acompañar la misión y la visión de la Universidad, sino para "
    "expresarlas. Estamos en el mismo camino.", body))

mv_style = S("mv", fontName="Helvetica", fontSize=9.5, leading=14, textColor=NAVY)
mv = Table([
    [Paragraph("<b>Misión · Universidad de Cuenca</b><br/><i>&ldquo;Formar investigadores y "
               "profesionales comprometidos con una sociedad justa, diversa y sostenible, dispuestos "
               "a ser agentes de transformación.&rdquo;</i>", mv_style)],
    [Paragraph("<b>Visión 2027</b><br/><i>&ldquo;Al 2027 la Universidad de Cuenca es una comunidad "
               "universitaria innovadora y resiliente, integrada al mundo a través de la generación "
               "de conocimiento pertinente, de calidad y comprometida con la sociedad.&rdquo;</i>", mv_style)],
], colWidths=[6.7 * inch])
mv.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
    ("LINEBEFORE", (0, 0), (0, -1), 3, ACCENT),
    ("LEFTPADDING", (0, 0), (-1, -1), 12),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("LINEBELOW", (0, 0), (0, 0), 0.5, colors.white),
]))
story.append(Spacer(1, 4))
story.append(mv)
story.append(Paragraph("Misión y visión oficiales de la Universidad de Cuenca (ucuenca.edu.ec).", small))
story.append(Spacer(1, 6))
story.append(Paragraph("Cómo este programa impulsa ambas", h2))
for t, d in [
    ("Generación de conocimiento pertinente y de calidad",
     "Estudios preregistrados y publicables en la frontera de la neurociencia producen exactamente "
     "el tipo de conocimiento original y socialmente significativo que plantea la visión."),
    ("Integrada al mundo",
     "Diseños de datos abiertos y de colaboración internacional conectan a Cuenca con la comunidad "
     "global que estudia la consciencia, invitando a alianzas entre laboratorios y disciplinas."),
    ("Agentes de transformación",
     "Formar investigadores de posgrado dentro de un programa audaz pero éticamente fundamentado "
     "moldea precisamente a los científicos transformadores que describe la misión."),
    ("Innovadora y resiliente",
     "Poner a prueba afirmaciones extraordinarias bajo condiciones limpias y falsables es innovación "
     "hecha con responsabilidad — y resiliente, porque incluso un resultado negativo es una "
     "contribución genuina."),
]:
    story.append(Paragraph(f"<b>{t}.</b> {d}", body))

story.append(Paragraph("Impacto global — Por qué importan los estudios de esta índole", h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "La consciencia sigue siendo una de las últimas grandes fronteras de la ciencia. Estudiarla con "
    "rigor —a través de estados psicodélicos extendidos, paradigmas cerebro a cerebro y la "
    "neurofisiología del trance— aborda preguntas fundamentales sobre la mente, el cerebro y la "
    "experiencia humana, con consecuencias que trascienden por mucho cualquier laboratorio "
    "individual.", body))
for t, d in [
    ("Salud mental",
     "La investigación de estados extendidos y psicodélicos ya está transformando los tratamientos "
     "para la depresión, el TEPT, las adicciones y el sufrimiento al final de la vida; datos locales "
     "rigurosos contribuyen directamente a ese esfuerzo global."),
    ("Un modelo de cómo la ciencia aborda lo extraordinario",
     "Llevar al laboratorio preguntas controvertidas pero importantes, bajo preregistro y datos "
     "abiertos, muestra cómo la ciencia debería poner a prueba afirmaciones audaces — sin "
     "descartarlas ni exagerarlas. Ese ejemplo metodológico es en sí mismo una contribución a la "
     "cultura científica."),
    ("Conocimiento en la frontera",
     "Un resultado positivo sería un hallazgo de referencia; un resultado nulo con potencia adecuada "
     "aclara los límites de estos fenómenos. En ambos casos, el conocimiento es nuevo, citable y "
     "capaz de dar forma al campo."),
    ("Cuenca en el mapa global",
     "Que una universidad de Ecuador lidere una investigación cuidadosa y ética sobre la consciencia "
     "es una declaración de que la ciencia de frontera puede hacerse en cualquier lugar — atrayendo "
     "colaboración, estudiantes y visibilidad internacional para la Universidad de Cuenca."),
]:
    story.append(Paragraph(f"<b>{t}.</b> {d}", body))

story.append(PageBreak())

# ---------------------------------------------------------------------------
# RESUMEN EJECUTIVO
# ---------------------------------------------------------------------------
story.append(Paragraph("Resumen ejecutivo", h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "Esta nota describe tres experimentos candidatos que podrían anclar una agenda de investigación "
    "en la Universidad de Cuenca sobre estados alterados de consciencia, neurofenomenología y el "
    "estudio científico de la experiencia humana extraordinaria. Cada uno se resume a continuación "
    "con una "
    "idea central, un diseño propuesto, la infraestructura requerida, consideraciones éticas y un "
    "presupuesto indicativo. Al final se incluyen una tabla comparativa de presupuestos y una "
    "cartera más amplia de diez candidatos adicionales.", body))

summary_rows = [
    [Paragraph("Estudio", tablehead), Paragraph("Pregunta central", tablehead),
     Paragraph("Presupuesto indicativo", tablehead), Paragraph("Riesgo / complejidad", tablehead)],
    [Paragraph("<b>1. DMT de estado extendido (DMTx)</b>", tablecellb),
     Paragraph("¿Puede el estado de DMT extenderse de forma segura y caracterizarse en tiempo real?", tablecell),
     Paragraph("$40k – $150k", tablecell),
     Paragraph("Alto — sustancia controlada, médico", tablecell)],
    [Paragraph("<b>2. Correlación cerebro a cerebro</b>", tablecellb),
     Paragraph("¿Muestran sujetos emparejados y separados respuestas de EEG correlacionadas?", tablecell),
     Paragraph("$17k – $55k", tablecell),
     Paragraph("Medio — el rigor del diseño lo es todo", tablecell)],
    [Paragraph("<b>3. Neurofisiología de trance / sanadores</b>", tablecellb),
     Paragraph("¿Entran los practicantes en un estado cerebral reproducible y distinto?", tablecell),
     Paragraph("$18k – $50k", tablecell),
     Paragraph("Bajo–Medio — limitado por reclutamiento", tablecell)],
]
st = Table(summary_rows, colWidths=[1.6 * inch, 2.45 * inch, 1.15 * inch, 1.5 * inch])
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
    "<b>Secuencia recomendada.</b> Los Estudios 2 y 3 son de menor costo, menor riesgo y más "
    "rápidos de aprobar éticamente; cualquiera podría servir como un primer proyecto creíble que "
    "demuestre rigor ante socios y financiadores. El Estudio 1 (DMTx) es el buque insignia "
    "científico, pero conlleva la mayor carga regulatoria, médica y presupuestaria, y conviene "
    "emprenderlo una vez que existan relaciones institucionales y un socio clínico.", body))


# ---------------------------------------------------------------------------
# Ayudante para un bloque de propuesta completo
# ---------------------------------------------------------------------------
def proposal(number, title, idea_html, design_items, equipment, ethics, timeline,
             budget_rows, budget_total, references, floor_note=None):
    story.append(PageBreak())
    band = Table([[Paragraph(f'<font color="white"><b>EXPERIMENTO {number}</b></font>', small)]],
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

    story.append(Paragraph("Idea central", h2))
    story.append(Paragraph(idea_html, body))

    story.append(Paragraph("Diseño propuesto", h2))
    for it in design_items:
        story.append(Paragraph(f"•&nbsp;&nbsp;{it}", bullet))
    story.append(Spacer(1, 4))

    eq_html = "<b>Infraestructura y equipamiento clave</b><br/>" + "<br/>".join(f"• {e}" for e in equipment)
    et_html = "<b>Consideraciones éticas y de seguridad</b><br/>" + "<br/>".join(f"• {e}" for e in ethics)
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

    story.append(Paragraph("Cronograma indicativo", h2))
    story.append(Paragraph(timeline, body))

    story.append(Paragraph("Presupuesto indicativo (aproximado / general)", h2))
    rows = [[Paragraph("Categoría de costo", tablehead), Paragraph("Estimación (USD)", tablehead)]]
    for cat, amt in budget_rows:
        rows.append([Paragraph(cat, tablecell), Paragraph(amt, tablecell)])
    rows.append([Paragraph("<b>Total indicativo</b>", tablecellb),
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
    if floor_note:
        story.append(Spacer(1, 4))
        story.append(Paragraph(floor_note, S("floor", fontName="Helvetica-Oblique", fontSize=9,
                                             leading=13, textColor=GREY)))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Referencias y enlaces clave", h2))
    for r in references:
        story.append(Paragraph(f'•&nbsp;<link href="{r[1]}" color="#1F6F8B">{r[0]}</link>', link))


# ---------------------------------------------------------------------------
# EXPERIMENTO 1
# ---------------------------------------------------------------------------
proposal(
    1,
    "DMT de Estado Extendido / DMTx",
    "En lugar de estudiar la DMT como una experiencia muy breve (5–15 minutos), este protocolo "
    "utiliza una dosis de carga intravenosa controlada seguida de una infusión de mantenimiento "
    "controlada por objetivo para <b>extender y estabilizar el estado de DMT</b> durante una ventana "
    "útil experimentalmente. Esto permite estudiar la fenomenología, los correlatos neuronales y "
    "cualquier estructura recurrente de la experiencia mientras se recopilan datos fisiológicos y de "
    "neuroimagen en tiempo real. La idea informal de DMT / percepción láser que conversamos se "
    "ubicaría dentro de este marco como un subestudio perceptual pequeño y ciego, en lugar de ser "
    "el objetivo principal.",
    [
        "<b>Diseño:</b> piloto farmacocinético / farmacodinámico abierto, n ≈ 8–12 voluntarios "
        "sanos con experiencia psicodélica, escalada de dosis intrasujeto.",
        "<b>Resultados primarios:</b> seguridad y tolerabilidad de la infusión extendida; viabilidad "
        "de mantener un estado subjetivo estable en un nivel plasmático objetivo.",
        "<b>Resultados secundarios:</b> firmas de EEG (potencia espectral, complejidad / entropía, "
        "conectividad); escalas de fenomenología validadas; entrevistas estructuradas posteriores a "
        "la sesión.",
        "<b>Subestudio ciego opcional:</b> tareas perceptuales aleatorizadas y ciegas administradas "
        "durante el estado estable para poner a prueba afirmaciones específicas bajo condiciones "
        "controladas.",
        "<b>Análisis:</b> preregistrado, con reglas de detención por seguridad y criterios primarios "
        "predefinidos.",
    ],
    [
        "Unidad de investigación clínica con monitoreo de grado anestésico (hospital aliado)",
        "Bomba(s) de infusión IV controlada(s) por objetivo — prestada(s)",
        "EEG de grado investigativo y monitoreo fisiológico — prestado",
        "DMT de grado farmacéutico y manejo por farmacia hospitalaria",
        "Almacenamiento de sustancias controladas y cadena de custodia",
    ],
    [
        "Licencias de sustancias controladas y permisos de importación (regulación ecuatoriana)",
        "Revisión completa por comité de ética de investigación (IRB)",
        "Médico en sitio y capacidad de reanimación",
        "Tamizaje riguroso; exclusiones cardíacas y psiquiátricas",
        "Apoyo psicológico capacitado e integración",
    ],
    "Aproximadamente 18–24 meses: 6–9 meses para lo regulatorio, ético y el suministro del fármaco; "
    "3 meses de montaje y capacitación del personal; 6–9 meses de recolección de datos; 3–6 meses "
    "de análisis y redacción.",
    [
        ("Permisos regulatorios, éticos y de sustancias controladas (Ecuador)", "$8,000"),
        ("Suministro de DMT de grado farmacéutico y manejo seguro", "$20,000"),
        ("Personal clínico y médico (médico, anestesia, enfermería, psiquiatra) — tarifas locales", "$25,000"),
        ("EEG / monitoreo prestado — acceso, transporte, calibración e insumos", "$8,000"),
        ("Personal de investigación principal (IP, posdoc, asistentes, analista — ~1 año, tarifas de Cuenca)", "$40,000"),
        ("Tamizaje de participantes, compensación e instalaciones", "$8,000"),
        ("Análisis de datos, cómputo, difusión y contingencia", "$6,000"),
    ],
    "≈ $90,000 – $150,000  (costos completos)",
    [
        ("Gallimore y Strassman (2016), Frontiers in Pharmacology",
         "https://doi.org/10.3389/fphar.2016.00211"),
        ("Estudio de DMT extendida (PMC10851633)",
         "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10851633/"),
        ("Estudio de infusión continua de DMT (PMC12032411)",
         "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12032411/"),
    ],
    floor_note="Con el máximo apoyo institucional en especie —síntesis del fármaco donada, "
    "colaboradores clínicos que participan como coinvestigadores, instrumentación prestada e "
    "investigadores de posgrado que integran el trabajo en sus tesis— el piso apalancado por "
    "alianzas baja a aproximadamente $40,000.",
)

# ---------------------------------------------------------------------------
# EXPERIMENTO 2
# ---------------------------------------------------------------------------
proposal(
    2,
    "Correlación Cerebro a Cerebro / Replicación del &ldquo;Potencial Transferido&rdquo;",
    "Inspirado en el controvertido trabajo de Jacobo Grinberg sobre los &ldquo;potenciales "
    "transferidos&rdquo;, en el que dos personas se ubican en habitaciones separadas, una recibe un "
    "estímulo y se monitorea la actividad cerebral de la otra en busca de respuestas correlacionadas. "
    "La afirmación es extraordinaria — y es precisamente por eso que merece una "
    "<b>replicación moderna y rigurosamente controlada</b>. El valor científico radica casi por "
    "completo en la calidad del diseño: doble ciego, blindaje, temporización aleatorizada y un "
    "análisis totalmente automatizado y preregistrado eliminan las brechas que hicieron imposible "
    "interpretar el trabajo original.",
    [
        "<b>Diseño:</b> estudio de EEG con sujetos emparejados, ≈ 25–30 parejas (con vínculo "
        "emocional y desconocidos), &ldquo;emisor&rdquo; y &ldquo;receptor&rdquo; en habitaciones "
        "separadas y blindadas electromagnéticamente.",
        "<b>Estímulo:</b> estímulos sensoriales aleatorizados y disparados por computadora al emisor "
        "en momentos desconocidos para el receptor y para todos los experimentadores presentes.",
        "<b>Resultado primario:</b> prueba preregistrada de actividad correlacionada y sincronizada "
        "en el tiempo en el EEG del receptor durante la estimulación del emisor frente a ventanas "
        "nulas equivalentes.",
        "<b>Controles:</b> bloques simulados/sin emisor, rechazo de artefactos a nivel de sensor y "
        "enmascaramiento del analista respecto a las etiquetas de condición.",
        "<b>Estadística:</b> umbral de tamaño de efecto preregistrado, criterios bayesianos + "
        "frecuentistas; un resultado nulo con potencia adecuada es un resultado publicable.",
    ],
    [
        "Dos sistemas de EEG de grado investigativo, sincronizados en el tiempo — prestados",
        "Habitaciones blindadas electromagnéticamente / aisladas tipo Faraday (instalación existente)",
        "Disparo por hardware e infraestructura de temporización de precisión",
        "Tubería de análisis automatizada y preregistrada",
        "Verificación de aislamiento de audio/RF",
    ],
    [
        "Aprobación ética / IRB (bajo riesgo físico)",
        "Consentimiento informado; derecho a retirarse",
        "Preregistro en OSF / AsPredicted antes de la recolección de datos",
        "Verificación independiente del aislamiento de las habitaciones",
        "Datos y código de análisis abiertos para total transparencia",
    ],
    "Aproximadamente 12–15 meses: 2–3 meses de ética y preregistro; 2 meses de montaje y pruebas de "
    "aislamiento; 5–6 meses de recolección de datos en parejas; 3–4 meses de análisis y redacción.",
    [
        ("EEG prestado — transporte, gorros/electrodos, gel, calibración", "$4,000"),
        ("Montaje de habitación blindada y pruebas de aislamiento (instalación existente)", "$5,000"),
        ("Personal principal (IP a tiempo parcial, posdoc, 2 asistentes, analista — ~1 año, tarifas de Cuenca)", "$30,000"),
        ("Reclutamiento y compensación de participantes (~60 participantes)", "$4,000"),
        ("Preregistro, diseño de replicación y asesoría estadística", "$3,000"),
        ("Cómputo, alojamiento de datos abiertos y difusión", "$2,000"),
    ],
    "≈ $35,000 – $55,000  (costos completos)",
    [
        ("Jacobo Grinberg — antecedentes y referencia de publicación (Wikipedia, ES)",
         "https://es.wikipedia.org/wiki/Jacobo_Grinberg"),
        ("Estudio relacionado de EEG con sujetos separados (PubMed 12972348)",
         "https://pubmed.ncbi.nlm.nih.gov/12972348/"),
    ],
    floor_note="Con instrumentación prestada, uso gratuito de una instalación blindada existente e "
    "investigadores estudiantes a cargo de la recolección de datos, el piso apalancado por alianzas "
    "baja a aproximadamente $17,000.",
)

# ---------------------------------------------------------------------------
# EXPERIMENTO 3
# ---------------------------------------------------------------------------
proposal(
    3,
    "Chamanes / Sanadores / Practicantes de Trance bajo EEG o fMRI",
    "Estudiar a chamanes, sanadores, meditadores o practicantes de trance mientras entran en su "
    "supuesto estado de sanación o estado alterado, y comparar su actividad cerebral y fisiología "
    "frente a controles equivalentes y frente a su propio reposo ordinario, imaginación y "
    "meditación. De manera crucial, este estudio <b>no</b> necesita comenzar afirmando que la "
    "&ldquo;energía sanadora&rdquo; es real. La primera pregunta científica, más sólida, es "
    "simplemente: <i>¿entran los practicantes capacitados en un estado neurofisiológico reproducible "
    "que sea medible y distinto de las líneas base ordinarias?</i> Si es así, una fase posterior "
    "puede poner a prueba si ese estado tiene algún efecto medible sobre los receptores.",
    [
        "<b>Diseño:</b> comparación intrasujeto de múltiples condiciones (trance vs. reposo vs. "
        "imaginería vs. meditación), ≈ 15–25 practicantes con experiencia + controles equivalentes.",
        "<b>Resultado primario:</b> firma de EEG/fMRI reproducible y específica del practicante que "
        "discrimine el estado de trance de las condiciones de control por encima del azar.",
        "<b>Resultados secundarios:</b> medidas autonómicas (VFC, actividad electrodérmica, "
        "respiración); clasificación del estado con aprendizaje automático validado de forma cruzada.",
        "<b>Fase 2 (opcional):</b> estudio ciego con receptores para detectar cualquier efecto "
        "fisiológico o perceptual sobre una segunda persona.",
        "<b>Análisis:</b> precisión de clasificación y umbrales de tamaño de efecto preregistrados.",
    ],
    [
        "Acceso a EEG y/o escáner de fMRI de grado investigativo — prestado",
        "Registro de fisiología autonómica / periférica (VFC, EDA) — prestado",
        "Audio-video sincronizado para anotación del estado",
        "Estación de análisis y tubería de aprendizaje automático",
        "Entorno de registro tranquilo y controlado",
    ],
    [
        "Aprobación ética / IRB; protocolo culturalmente respetuoso",
        "Consulta comunitaria y compensación justa para los practicantes",
        "Consentimiento informado que honre las tradiciones de los practicantes",
        "Encuadre claro de no afirmación médica en todos los materiales",
        "Preregistro de hipótesis y análisis",
    ],
    "Aproximadamente 12–18 meses: 2–3 meses de ética, vinculación comunitaria y reclutamiento; "
    "5–7 meses de recolección de datos (al ritmo del reclutamiento); 3–5 meses de análisis y "
    "redacción.",
    [
        ("EEG / fMRI prestado — tarifas de acceso al escáner e insumos (~40 sesiones)", "$5,000"),
        ("Personal principal (posdoc, asistentes, analista de datos — ~1 año, tarifas de Cuenca)", "$28,000"),
        ("Reclutamiento de practicantes, viajes y compensación", "$6,000"),
        ("Fisiología periférica (VFC, EDA) — prestada / de bajo costo", "$2,000"),
        ("Ética, preregistro, difusión y contingencia", "$3,000"),
    ],
    "≈ $30,000 – $50,000  (costos completos)",
    [
        ("Investigación sobre trance cognitivo / de estilo chamánico (arXiv 2509.19254)",
         "https://arxiv.org/abs/2509.19254"),
        ("Trance y neurofisiología — antecedentes generales (Wikipedia)",
         "https://en.wikipedia.org/wiki/Trance"),
    ],
    floor_note="Con tiempo de escáner / EEG donado, hardware de fisiología prestado e investigadores "
    "estudiantes liderando la recolección de datos, el piso apalancado por alianzas baja a "
    "aproximadamente $18,000.",
)

# ---------------------------------------------------------------------------
# PRESUPUESTO COMPARATIVO + NOTAS
# ---------------------------------------------------------------------------
story.append(PageBreak())
story.append(Paragraph("Panorama presupuestario comparativo", h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "Las cifras a continuación son <b>estimaciones aproximadas, de orden de magnitud</b>, para "
    "estudios piloto realizados en <b>Cuenca, Ecuador</b>, usando <b>salarios locales</b> y "
    "<b>equipamiento prestado</b> de instituciones aliadas (sin compras importantes de hardware). "
    "Cada estudio se muestra en dos escenarios: una cifra <b>apalancada por alianzas</b> que asume "
    "el máximo apoyo en especie, y una cifra con <b>costos completos</b> a precio de mercado. La "
    "mayor variable en ambos es el tiempo del personal calificado.", body))

comp = [
    [Paragraph("Estudio", tablehead), Paragraph("Apalancado por alianzas", tablehead),
     Paragraph("Costos completos", tablehead), Paragraph("Duración", tablehead),
     Paragraph("Rol", tablehead)],
    [Paragraph("1 · DMT de estado extendido (DMTx)", tablecellb), Paragraph("~$40k", tablecell),
     Paragraph("$150k", tablecell), Paragraph("18–24 meses", tablecell),
     Paragraph("Buque insignia — fase posterior", tablecell)],
    [Paragraph("2 · Correlación cerebro a cerebro", tablecellb), Paragraph("~$17k", tablecell),
     Paragraph("$55k", tablecell), Paragraph("12–15 meses", tablecell),
     Paragraph("Candidato fuerte", tablecell)],
    [Paragraph("3 · Neurofisiología de trance / sanadores", tablecellb), Paragraph("~$18k", tablecell),
     Paragraph("$50k", tablecell), Paragraph("12–18 meses", tablecell),
     Paragraph("Candidato fuerte", tablecell)],
    [Paragraph("<b>Programa combinado (los tres)</b>", tablecellb),
     Paragraph("<b>~$75k</b>", tablecellb), Paragraph("<b>$255k</b>", tablecellb),
     Paragraph("~2–3 años por fases", tablecell), Paragraph("—", tablecell)],
]
ct = Table(comp, colWidths=[2.05 * inch, 1.2 * inch, 1.0 * inch, 1.0 * inch, 1.45 * inch])
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
    "La columna <i>apalancado por alianzas</i> refleja el máximo apoyo en especie (equipamiento y "
    "tiempo de escáner donados, colaboradores que participan como coinvestigadores, recolección de "
    "datos liderada por estudiantes); la columna <i>costos completos</i> cotiza cada línea a precio "
    "de mercado. Un presupuesto operativo realista suele ubicarse entre ambos, ya que el tiempo del "
    "personal calificado es el costo menos comprimible. Los Estudios 2 y 3 son lo bastante modestos "
    "como para ejecutarse como proyectos de investigación de posgrado / de docentes; el Estudio 1 "
    "(DMTx) conlleva la carga clínica, farmacológica y regulatoria que lo mantiene como el más "
    "costoso incluso a precios locales.", small))

story.append(Paragraph("Principios transversales", h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=8))
for t, d in [
    ("Replicación, no defensa de una postura",
     "Cada estudio se plantea para ser publicable ya sea que el resultado sea positivo o nulo. "
     "Ponemos a prueba afirmaciones, no las defendemos."),
    ("Preregistro por defecto",
     "Las hipótesis, los tamaños de muestra y los planes de análisis se registran antes de la "
     "recolección de datos en OSF o una plataforma comparable, protegiendo contra el sesgo y las "
     "narrativas post hoc."),
    ("La ética primero",
     "Cada estudio está diseñado para ser aprobable éticamente en una universidad convencional, con "
     "la revisión, el consentimiento, la seguridad y (para el Estudio 3) el respeto cultural "
     "apropiados."),
    ("Abierto y transparente",
     "Datos y código de análisis abiertos siempre que sea éticamente posible, para que los "
     "resultados puedan verificarse de forma independiente — la salvaguarda más importante para "
     "preguntas controvertidas."),
]:
    story.append(Paragraph(f"<b>{t}.</b> {d}", body))

# Cartera más amplia
story.append(Paragraph("Cartera más amplia — Diez candidatos adicionales", h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "Más allá de los tres estudios prioritarios, los siguientes son sólidos candidatos adicionales "
    "de replicación en la investigación sobre consciencia y estados alterados, disponibles para "
    "construir un programa más amplio:", body))
pipeline = [
    "Comunicación en tiempo real con soñadores lúcidos durante el sueño REM",
    "Psilocibina y mayor repertorio de estados cerebrales",
    "Ayahuasca y entropía cerebral / reorganización de redes",
    "Meditadores expertos y sincronía gamma de alta amplitud",
    "Hipnosis y cambios en el dolor, la agencia y la autopercepción",
    "Estados no ordinarios inducidos por respiración (breathwork) sin psicodélicos",
    "Ganzfeld / privación sensorial y percepción generada internamente",
    "Experiencias cercanas a la muerte y actividad cerebral al final de la vida",
    "Anestesia y complejidad perturbacional como medida de la consciencia",
    "Transferencia corporal en realidad virtual o ilusión extracorporal",
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
    "Preparada por Ney Torres · 23 de junio de 2026 · Borrador de nota conceptual para discusión "
    "con la Universidad de Cuenca. Todas las cifras presupuestarias son indicativas y están sujetas "
    "a refinamiento con la institución anfitriona.", small))

doc.build(story)
print("WROTE", OUTPUT)
