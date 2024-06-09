from fpdf import FPDF

class Shirtificate:

    pdf = FPDF(orientation = "portrait", format = 'A4')
    pdf.add_page()
    pdf.set_fill_color(255,255,255)
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.set_font('helvetica', style="B", size = 50) 
    pdf.cell(0, 60, 'CS50P Shirtificate', align='C')
    pdf.image("shirtificate.png", (pdf.w - pdf.epw)/2, 100, pdf.epw, 0)

    @classmethod
    def take_shirt(cls, name):
        cls.pdf.set_font('helvetica',style= "BI", size = 25)
        cls.pdf.set_text_color(255,255,255)
        cls.pdf.ln(90)
        cls.pdf.cell(0,100,f"{name} took CS50P", align='C')
        cls.pdf.output('shirtificate.pdf')

Shirtificate.take_shirt(input("What's your name? "))