from pypdf import PdfWriter
import os

#making instance of pdfwriter
merger=PdfWriter()#The Main Lines 1

pdfs_path="./pdfs"

#extracting pdf files from folder
pdf_files=[]
for f in os.listdir(pdfs_path):
    if f.endswith(".pdf"):
      pdf_files.append(os.path.join(pdfs_path, f))
pdf_files.sort()

#merging process
try:
    for pdf in pdf_files:
          merger.append(pdf)#Main Line 2
    merger.write("output.pdf")#Main Line 3
except Exception as e:
    print(f"An Error Occurred : {e}")
finally:
    merger.close()