from fpdf import FPDF
import os

os.makedirs("challans", exist_ok=True)

def generate_challan(plate, fine, image):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Traffic Challan", ln=True, align='C')

    pdf.cell(200, 10, txt=f"Vehicle: {plate}", ln=True)
    pdf.cell(200, 10, txt=f"Fine: ₹{fine}", ln=True)

    pdf.image(image, x=10, y=50, w=100)

    filename = f"challans/{plate}.pdf"
    pdf.output(filename)