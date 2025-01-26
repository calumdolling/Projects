 # -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "This is a test file, I am reading this out to you")
    c.save()

if __name__ == "__main__":
    create_pdf("test_file.pdf")