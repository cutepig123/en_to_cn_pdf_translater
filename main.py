import sys
import os
import fnmatch

import logging, coloredlogs

coloredlogs.install()
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
#print = lambda *tup : logging.info(str(" ".join([str(x) for x in tup]))) 

logging.info('from logging')
logging.error('error from logging')

inc_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(inc_path)

import lib.trans
import lib.docx_add_heading
import lib.docx2pdf

def dummy(file_in, file_out):
    #print(file_in, file_out)
    pass

STEPS = [
#    ['.pdf', dummy],
    ['.docx', lib.trans.trans],
    ['.docx-cn.docx', lib.docx_add_heading.add_heading],
    ['.docx-cn-contents.docx', lib.docx2pdf.docx2pdf],
    ['.docx-cn-contents.pdf', dummy],
]

N_STEPS = len(STEPS)

EXTS_SKIP = ['*-cn.pdf', '*.docx-0.??-cn.docx', '*\\~$*']

assert(fnmatch.fnmatch('xx-cn.pdf','*-cn.pdf'))

def main_file(file):
    for ext in EXTS_SKIP:
        if fnmatch.fnmatch(file,ext):
            return

    file_no_ext = None
    curr_step = None
    for i in range(N_STEPS-1, -1, -1):
        ext = STEPS[i][0]
        if file.endswith(ext):
            file_no_ext = file[:-len(ext)]
            break
    if file_no_ext is None:
        return
    for i in range(N_STEPS-1, -1, -1):
        ext = STEPS[i][0]
        file_w_ext = file_no_ext + ext
        if os.path.isfile(file_w_ext):
            curr_step = i
            print(file_no_ext, curr_step)
            break
    if curr_step is not None:
        for i in range(curr_step, N_STEPS-1):
            ext = STEPS[i][0]
            ext_des = STEPS[i+1][0]
            fn = STEPS[i][1]
            file_src = file_no_ext + ext
            file_des = file_no_ext + ext_des
            fn(file_src, file_des)

def main_folder(folder):
    for file in os.listdir(folder):
        main_file(folder + '\\' + file)

folder = sys.argv[1] if len(sys.argv)>1 else r'g:\done'
print(folder)
main_folder(folder)
