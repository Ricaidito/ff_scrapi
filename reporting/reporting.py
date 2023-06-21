import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Define the PDF file path
path = "reporting/reports/"
pdf_filename = path + "prices_report.pdf"

# Retrieve data from your list of dictionaries
# Replace the following line with your MongoDB retrieval code
data = [
    {
        "id": "1",
        "Nombre": "Aceite",
        "Precio": "RD$ 96",
        "Categoría": "Canasta básica",
        "Fecha de extración": "2023-06-20",
    },
    {
        "id": "2",
        "Nombre": "Pollo",
        "Precio": "RD$ 201",
        "Categoría": "Canasta básica",
        "Fecha de extración": "2023-06-20",
    },
    {
        "id": "3",
        "Nombre": "Arroz",
        "Precio": "RD$ 383",
        "Categoría": "Canasta básica",
        "Fecha de extración": "2023-06-20",
    },
    {
        "id": "4",
        "Nombre": "Filete de res",
        "Precio": "RD$ 197",
        "Categoría": "Canasta básica",
        "Fecha de extración": "2023-06-20",
    },
    {
        "id": "5",
        "Nombre": "Plátano verde",
        "Precio": "RD$ 15 unid.",
        "Categoría": "Canasta básica",
        "Fecha de extración": "2023-06-20",
    },
]

# Convert the list of dictionaries to a pandas DataFrame, excluding the "id" field
df = pd.DataFrame(data).drop("id", axis=1)

# Create a SimpleDocTemplate object with the specified PDF filename
pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Convert the pandas DataFrame to a list of lists
table_data = [df.columns.tolist()] + df.values.tolist()

# Create the table and set its style
table = Table(table_data)
table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]
    )
)

# Create title and subtitle paragraphs
title_text = "Food Forecast"
subtitle_text = "Report"

styles = getSampleStyleSheet()
title_paragraph = Paragraph(title_text, styles["Heading1"])
subtitle_paragraph = Paragraph(subtitle_text, styles["Heading2"])

# Build the PDF document
elements = [title_paragraph, subtitle_paragraph, table]
pdf.build(elements)
print(f"PDF file '{pdf_filename}' has been generated.")
