from fpdf import FPDF
from fpdf.enums import XPos, YPos

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Helvetica", size=16, style="B")
        self.cell(0,10,"CS50 Shirtificate", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(10)

def create_shirtificate(name):
    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    shirt_image_path = "shirtificate.png"
    image_x = (210-190)/2
    pdf.image(shirt_image_path, x=image_x, y=70, w=190)

    pdf.set_xy(0,150)
    pdf.set_font("Helvetica", size=24, style="B")
    pdf.set_text_color(255,255,255)
    pdf.cell(210,10,f"{name} took CS50", align="C")

    output_path = "shirtificate.pdf"
    pdf.output(output_path)
    print(f"Shirtificate saved as {output_path}")

if __name__ == "__main__":
    name = input("Name: ").strip()
    create_shirtificate(name)
