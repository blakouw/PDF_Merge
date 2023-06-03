import PyPDF2
import os

merging = PyPDF2.PdfMerger()
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merging.append(file)
    merging.write("MERGED")

print("Merging done")