import sys
import os

inc_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(inc_path)

import lib.trans
import lib.docx_add_heading
import lib.docx2pdf

def dummy(file_in, file_out):
    #print(file_in, file_out)
    pass

STEPS = [
    ['.pdf', dummy],
    ['.docx', lib.trans.trans],
    ['.docx-cn.docx', lib.docx_add_heading.add_heading],
    ['.docx-cn-contents.docx', lib.docx2pdf.docx2pdf],
    ['.docx-cn-contents.pdf', dummy],
]

N_STEPS = len(STEPS)

EXTS_SKIP = ['-cn.pdf']

def main_file(file):
    for ext in EXTS_SKIP:
        if file.endswith(ext):
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

main_folder(r'g:\done')
