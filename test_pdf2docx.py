import sys
import os
import glob
import win32com.client
import os
from pdf2docx import parse

fname = sys.argv[1] if len(
    sys.argv) > 1 else r'G:\\'

class WordConverter:
    def __init__(self):
        self.word = win32com.client.Dispatch("Word.Application")
        self.word.visible = True

    def convert(self, in_file):
        wb = self.word.Documents.Open(in_file)
        out_file = in_file[0:-4] + ".docx"
        wb.SaveAs2(out_file, FileFormat=16) # file format for docx
        wb.Close()

    def __del__(self):
        self.word.Quit()

class pdf2docxConverter:
    def convert(self, in_file):
        parse(in_file)

converter = WordConverter()
#converter = pdf2docxConverter()

def convert(in_file):
    converter.convert(in_file)
    

if __name__ == '__main__':
    if os.path.isfile(fname):
        convert(fname)
    else:
        folder_name = fname
        os.chdir(folder_name)

        for filename in os.listdir(folder_name):
            # a file has following types
            #   is a transted file
            #   is a non translated file, and there is no correponding translated file
            is_pdf = filename.lower().endswith('.pdf')
            is_cn_pdf = filename.lower().endswith('-cn.pdf')
            if is_pdf and not is_cn_pdf:
                docx_file_name = '{}.docx'.format(filename[:-len('.pdf')])
                if not os.path.isfile(docx_file_name):
                    print(filename)
                    convert('%s\\%s'%(folder_name,filename))


