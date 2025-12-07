from reportlab.pdfgen import canvas

def create_pdf(stress, exercise):
    file_path = "stress_report.pdf"
    c = canvas.Canvas(file_path)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, 780, "Weekly Stress Report")

    c.setFont("Helvetica", 14)
    c.drawString(50, 740, f"Predicted Stress Level: {stress}")
    c.drawString(50, 710, "Recommended Routine:")
    c.drawString(60, 690, f"- {exercise}")
    c.drawString(50, 660, "Follow these daily and track improvements!")

    c.save()
    return file_path