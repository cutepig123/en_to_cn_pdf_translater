import sys
import os
from docx2pdf import convert

fname = sys.argv[1] if len(
    sys.argv) > 1 else r'G:\\'
if __name__ == '__main__':
    if os.path.isfile(fname):
        convert(fname)
    else:
        #from multiprocessing import Process
        os.chdir(fname)

        for filename in os.listdir(fname):
            # a file has following types
            #   is a transted file
            #   is a non translated file, and there is no correponding translated file
            is_translated_file = filename.lower().endswith('.docx-cn.docx')
            if is_translated_file:
                pdf_file_name = '{}.pdf'.format(filename[:-len('.docx')])
                if not os.path.isfile(pdf_file_name):
                    print(filename)
       
