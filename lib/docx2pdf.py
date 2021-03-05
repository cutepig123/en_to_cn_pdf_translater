import sys
import os
# from docx2pdf import convert

# def docx2pdf(src, des):
#     convert(src, des)

import win32com.client

def docx2pdf(src, des):
    word = win32com.client.Dispatch("Word.Application")
    wdFormatPDF = 17

    doc = word.Documents.Open(src)
    #doc.SaveAs(str(pdf_filepath), FileFormat=wdFormatPDF)
    doc.ExportAsFixedFormat(OutputFileName=des,
        ExportFormat=17, #17 = PDF output, 18=XPS output
        OpenAfterExport=False,
        OptimizeFor=0,  #0=Print (higher res), 1=Screen (lower res)
        CreateBookmarks=1, #0=No bookmarks, 1=Heading bookmarks only, 2=bookmarks match word bookmarks
        DocStructureTags=True
        )
        
    doc.Close()

    word.Quit()
    return True