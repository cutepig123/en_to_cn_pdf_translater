import sys
import os
from docx import Document


def add_heading(file):
    document = Document(file)
    # 显示每段的内容
    for p in document.paragraphs:
        print(p.text)
        print(p.text_2)
        if p.text.lower().startswith('chapter'):
            print ('change style to heading')
            p.style = 'Heading 1'

    # 添加段落
    document.add_paragraph('这是新的段落内容')
    # 保存文档
    document.save(file)

add_heading(r'G:\done\CUDA by Example An Introduction to General-Purpose GPU Programming by Jason Sanders, Edward Kandrot (z-lib.org).docx-cn.docx')
pause

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
                    convert(filename)
