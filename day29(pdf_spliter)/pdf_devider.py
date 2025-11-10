from pypdf import PdfReader,PdfWriter
import os

def pdfspliter(input_path,output_path,start_page,end_page):
    if not input_path:
        return "⚠️input Pdf Path is Empty"
    if not output_path:
        return "⚠️output Pdf Path is Empty"
    if not start_page:
        return "⚠️Starting index is Empty"
    if not end_page:
        return "⚠️Ending index is Empty"
    if os.path.exists(input_path):
        pass
    else:
        return f"⚠️Invalid pdf path"
    if os.path.exists(output_path):
        pass
    else:
        return "⚠️Invalid output directory"
    reader=PdfReader(input_path)
    writer = PdfWriter()
    start_page=int(start_page)
    end_page=int(end_page)
    if start_page<1 or start_page>len(reader.pages) or end_page>len(reader.pages) or end_page<start_page:
       return f"Invalid Index , please enter in range of pdf"
    else:
        pass
    for i in range((start_page-1),end_page):
        writer.add_page(reader.pages[i])
        output_filename = f"{output_path}/new.pdf"
        with open(f"{output_filename}","wb") as f:
              writer.write(f)
    return f"Pdf sucessfully Splitted from index {start_page} to {end_page}  ✅"


