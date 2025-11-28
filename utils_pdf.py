# utils_pdf.py
# -----------------------------------------------------------
# TripWeave PDF generator
# -----------------------------------------------------------
from io import BytesIO
from collections import defaultdict

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)
from reportlab.lib.units import cm


def _build_styles():
    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="TitleMain",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=28,
            textColor=colors.HexColor("#2563eb"),  # blue
            spaceAfter=16,
        )
    )

    styles.add(
        ParagraphStyle(
            name="Subtitle",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=11,
            leading=14,
            textColor=colors.HexColor("#4b5563"),
            spaceAfter=10,
        )
    )

    styles.add(
        ParagraphStyle(
            name="SectionHeading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=16,
            leading=19,
            textColor=colors.HexColor("#111827"),
            spaceBefore=18,
            spaceAfter=8,
        )
    )

    styles.add(
        ParagraphStyle(
            name="DayHeading",
            parent=styles["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=17,
            textColor=colors.HexColor("#1d4ed8"),
            spaceBefore=14,
            spaceAfter=6,
        )
    )

    styles.add(
        ParagraphStyle(
            name="Small",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#6b7280"),
        )
    )

    return styles


def build_itinerary_pdf(
    schedule,
    destination: str,
    trip_days: int,
    travel_style: str,
    per_day_budget: float,
    weather_pref: str,
    energy_morning: str,
    energy_afternoon: str,
    energy_evening: str,
):
    """
    Build a TripWeave itinerary PDF and return it as bytes.

    schedule: list of dicts with keys:
        "Day", "Time", "Energy", "Activity", "Category",
        "Indoor / Outdoor", "Estimated Cost (₹)", "Maps Link"
    """

    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = _build_styles()
    story = []

    # ---------------------- COVER / TITLE ----------------------
    title_text = "TripWeave – Your TECE-Powered Itinerary"
    story.append(Paragraph(title_text, styles["TitleMain"]))

    subtitle_text = (
        f"Destination: <b>{destination}</b> &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"Days: <b>{trip_days}</b> &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"Style: <b>{travel_style}</b>"
    )
    story.append(Paragraph(subtitle_text, styles["Subtitle"]))

    # Summary section
    story.append(Paragraph("Trip Summary", styles["SectionHeading"]))
    summary_lines = [
        f"• Estimated budget per day: <b>₹{int(per_day_budget)}</b>",
        f"• Weather context: <b>{weather_pref}</b>",
        (
            "• Energy curve: "
            f"<b>Morning-{energy_morning}</b>, "
            f"<b>Afternoon-{energy_afternoon}</b>, "
            f"<b>Evening-{energy_evening}</b>"
        ),
    ]
    for line in summary_lines:
        story.append(Paragraph(line, styles["Normal"]))
    story.append(Spacer(1, 12))

    # ---------------------- ORGANIZE BY DAY ----------------------
    by_day = defaultdict(list)
    for row in schedule:
        by_day[row["Day"]].append(row)

    # Sort days
    for day in sorted(by_day.keys()):
        day_rows = by_day[day]

        # Day heading
        story.append(Paragraph(f"Day {day}", styles["DayHeading"]))

        # Build table data
        table_data = [
            [
                "Time",
                "Energy",
                "Activity",
                "Category",
                "Indoor/Outdoor",
                "Est. Cost (₹)",
            ]
        ]

        for r in day_rows:
            table_data.append(
                [
                    r["Time"],
                    r["Energy"],
                    r["Activity"],
                    r["Category"],
                    r["Indoor / Outdoor"],
                    str(r["Estimated Cost (₹)"]),
                ]
            )

        table = Table(table_data, colWidths=[2.2 * cm, 2.1 * cm, 6.0 * cm, 2.8 * cm, 2.6 * cm, 2.4 * cm])
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1e293b")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 9),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                    ("TEXTCOLOR", (0, 1), (-1, -1), colors.HexColor("#111827")),
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                    ("FONTSIZE", (0, 1), (-1, -1), 8),
                    ("ALIGN", (0, 1), (1, -1), "CENTER"),
                    ("ALIGN", (2, 1), (-1, -1), "LEFT"),
                    ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#cbd5e1")),
                ]
            )
        )
        story.append(table)
        story.append(Spacer(1, 8))

        # Maps section (small)
        story.append(Paragraph("Map Links", styles["Small"]))
        for r in day_rows:
            maps_line = (
                f"• Day {day} – {r['Time']} – {r['Activity']}: "
                f"<font color='#2563eb'>{r['Maps Link']}</font>"
            )
            story.append(Paragraph(maps_line, styles["Small"]))
        story.append(Spacer(1, 12))

        # Page break after day, if many days
        if day != sorted(by_day.keys())[-1]:
            story.append(PageBreak())

    # Footer note
    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            "Generated by <b>TripWeave</b> – Micro-SaaS Travel Planner (TECE Engine).",
            styles["Small"],
        )
    )

    # Build PDF
    doc.build(story)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes
