import os
import sqlite3
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"
OUTPUT_PATH = BASE_DIR / "static" / "files" / "resume.pdf"


def para(text, style):
    return Paragraph(str(text).replace("\n", "<br/>"), style)


def section_title(text, styles):
    return [
        Spacer(1, 0.16 * inch),
        Paragraph(text, styles["SectionTitle"]),
        HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#d9e2ef")),
        Spacer(1, 0.08 * inch),
    ]


def rows(table, order_by):
    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        return connection.execute(f"SELECT * FROM {table} ORDER BY {order_by}").fetchall()


def duration(row):
    start = row["start_date"][:7]
    start_year, start_month = start.split("-")
    month_names = {
        "01": "Jan",
        "02": "Feb",
        "03": "Mar",
        "04": "Apr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Aug",
        "09": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec",
    }
    start_label = f"{month_names[start_month]} {start_year}"
    if row["end_date"]:
        end_year, end_month = row["end_date"][:7].split("-")
        end_label = f"{month_names[end_month]} {end_year}"
    else:
        end_label = "Present"
    return f"{start_label} - {end_label}"


def clean_bullet(line):
    return line.strip().lstrip("-*•").strip()


def build_pdf():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=A4,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.45 * inch,
        title="Shubham Singh Resume",
        author="Shubham Singh",
    )

    base = getSampleStyleSheet()
    styles = {
        "Name": ParagraphStyle(
            "Name",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=28,
            textColor=colors.HexColor("#172033"),
            spaceAfter=2,
        ),
        "Subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["BodyText"],
            fontSize=10,
            leading=13,
            textColor=colors.HexColor("#4f5f75"),
            spaceAfter=4,
        ),
        "Contact": ParagraphStyle(
            "Contact",
            parent=base["BodyText"],
            fontSize=8.7,
            leading=11,
            textColor=colors.HexColor("#455468"),
            spaceAfter=2,
        ),
        "SectionTitle": ParagraphStyle(
            "SectionTitle",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            textColor=colors.HexColor("#0d6efd"),
            spaceAfter=2,
        ),
        "Body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontSize=9.2,
            leading=12.4,
            textColor=colors.HexColor("#29384d"),
            spaceAfter=5,
        ),
        "Small": ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontSize=8.7,
            leading=11.5,
            textColor=colors.HexColor("#4f5f75"),
            spaceAfter=4,
        ),
        "Role": ParagraphStyle(
            "Role",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10.2,
            leading=13,
            textColor=colors.HexColor("#172033"),
            spaceAfter=1,
        ),
        "Meta": ParagraphStyle(
            "Meta",
            parent=base["BodyText"],
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#607086"),
            spaceAfter=4,
        ),
        "Skill": ParagraphStyle(
            "Skill",
            parent=base["BodyText"],
            fontSize=8.8,
            leading=11.5,
            textColor=colors.HexColor("#29384d"),
            leftIndent=8,
            firstLineIndent=-8,
        ),
    }

    story = [
        Paragraph("Shubham Singh", styles["Name"]),
        Paragraph("Data Analyst | Business Intelligence Developer | Automation Enthusiast", styles["Subtitle"]),
        Paragraph(
            "Phone: +91 9520132466 | Email: shubhamsinghh057@gmail.com | "
            "LinkedIn: linkedin.com/in/shubham469 | GitHub: github.com/Shubham469",
            styles["Contact"],
        ),
    ]

    story += section_title("Professional Summary", styles)
    story.append(
        Paragraph(
            "Data Analyst with 3 years experience in translating business requirements into actionable insights, "
            "developing data-driven dashboards, and streamlining reporting processes. Skilled in Power BI, SQL, "
            "and data warehousing with experience in stakeholder management, process improvement, and KPI tracking. "
            "Adept at bridging the gap between business needs and technical solutions to drive informed decision-making.",
            styles["Body"],
        )
    )

    skills = rows("portfolio_skill", "category, \"order\", name")
    if skills:
        story += section_title("Skills & Technical Competencies", styles)
        current_category = None
        for skill in skills:
            if skill["category"] != current_category:
                current_category = skill["category"]
                story.append(Paragraph(f"<b>{current_category}</b>", styles["Small"]))
            story.append(Paragraph(f"- {skill['name']}", styles["Skill"]))

    experiences = rows("portfolio_experience", "\"order\", start_date DESC")
    if experiences:
        story += section_title("Professional Experience", styles)
        for exp in experiences:
            story.append(Paragraph(exp["title"], styles["Role"]))
            location = f" | {exp['location']}" if exp["location"] else ""
            story.append(Paragraph(f"{exp['company']}{location} | {duration(exp)}", styles["Meta"]))
            for line in exp["description"].splitlines():
                item = clean_bullet(line)
                if item:
                    story.append(Paragraph(f"- {item}", styles["Skill"]))
            story.append(Spacer(1, 0.05 * inch))

    educations = rows("portfolio_education", "\"order\", year_end DESC")
    if educations:
        story += section_title("Education", styles)
        for edu in educations:
            story.append(Paragraph(f"<b>{edu['degree']}</b> | {edu['institution']} | {edu['year_end']}", styles["Small"]))
            if edu["description"]:
                story.append(Paragraph(edu["description"], styles["Small"]))

    certifications = rows("portfolio_certification", "\"order\", year DESC")
    if certifications:
        story += section_title("Certifications", styles)
        for cert in certifications:
            story.append(Paragraph(f"<b>{cert['title']}</b> | {cert['issuer']} ({cert['year']})", styles["Small"]))

    doc.build(story)
    print(OUTPUT_PATH)


if __name__ == "__main__":
    build_pdf()
