from PyPDF2 import PdfReader

pdf_path = r'c:\Users\John Joseph Perez\Downloads\csc120\hess-main\hess-main\perez-ite18\updated_resume.pdf'
reader = PdfReader(pdf_path)
text = ''
for page in reader.pages:
    text += page.extract_text()
print(text)
