import os
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf():
    # 🔥 Ensure folder exists
    os.makedirs("knowledge_base", exist_ok=True)

    file_path = "knowledge_base/support.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = [
        Paragraph("Customer Support Knowledge Base", styles["Title"]),

        Paragraph("Reset password: Go to settings and click reset password.", styles["Normal"]),

        Paragraph("Refund policy: Customers can request a refund within 30 days of purchase.", styles["Normal"]),

        Paragraph("Login issue: Clear browser cache or reset your password.", styles["Normal"]),

        Paragraph("Account locked: Wait 15 minutes or contact support.", styles["Normal"]),
    ]

    doc.build(content)

    print(f"✅ Knowledge base created at: {file_path}")


if __name__ == "__main__":
    create_pdf()