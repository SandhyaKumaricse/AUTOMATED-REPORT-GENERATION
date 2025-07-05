import csv
from fpdf import FPDF


file_path = 'data.csv'
names = []
scores = []

with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        names.append(row['Name'])
        scores.append(int(row['Score']))

# Analysis
average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

# Generating the PDF Report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Automated Score Report", ln=True, align='C')

pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(100, 10, txt="Name", border=1)
pdf.cell(50, 10, txt="Score", border=1)
pdf.ln()

pdf.set_font("Arial", size=12)
for name, score in zip(names, scores):
    pdf.cell(100, 10, txt=name, border=1)
    pdf.cell(50, 10, txt=str(score), border=1)
    pdf.ln()

# Summary
pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, txt="Summary:", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, txt=f"Average Score: {average_score:.2f}", ln=True)
pdf.cell(0, 10, txt=f"Highest Score: {highest_score}", ln=True)
pdf.cell(0, 10, txt=f"Lowest Score: {lowest_score}", ln=True)

# Saving the PDF
pdf.output("report.pdf")
