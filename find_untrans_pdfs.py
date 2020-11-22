import os, sys

#idea 
#Find all translated files and move to 'done' folder, by: ends with .docx-cn.docx,
#

path=r'G:\\'
if len(sys.argv)>1:
    path=sys.argv[1]

def MySystem(cmd):
    print(cmd)
    os.system(cmd)

os.chdir(path)

MySystem('md done')

base_files_translated = []
for file in os.listdir(path):
    is_translated = file.lower().endswith('.docx-cn.docx')
    if is_translated:
        base_files_translated.append(file[:-len('.docx-cn.docx')])

for file_name_no_ext in  base_files_translated: 
    #file_name_no_ext = os.path.basename(file)
    pdf_file = '{}.pdf'.format(file_name_no_ext)
    doc_file = '{}.doc'.format(file_name_no_ext)
    docx_file = '{}.docx'.format(file_name_no_ext)
    docx_cn_file = '{}.docx-cn.docx'.format(file_name_no_ext)
    if os.path.isfile(pdf_file):
        MySystem('move "%s" done\\'%pdf_file)
    if os.path.isfile(doc_file):
        MySystem('move "%s" done\\'%doc_file)
    if os.path.isfile(docx_file):
        MySystem('move "%s" done\\'%docx_file)
    if os.path.isfile(docx_cn_file):
        MySystem('move "%s" done\\'%docx_cn_file)
    for i in range(10):
        partial_docx_cn_file = '%s.docx-%.2f-cn.docx'%(file_name_no_ext, 0.1*i)
        if os.path.isfile(partial_docx_cn_file):
            MySystem('del "%s"'%partial_docx_cn_file)
       