from googletrans import Translator
import sys

fname = sys.argv[1] if len(
    sys.argv) > 1 else r'F:\GoogleDriveSync3\jobrelated\The Fast Forward MBA in Project Management ( PDFDrive.com ).full.txt'


def next_str(cont):
    i = 0
    N = 5000
    L = len(cont)
    while i < L:
        print(1.0*i/L)
        if i+N >= L:
            return cont[i:]
        else:
            i2 = i+N
            subCont = cont[i:i2]

            # Find last \n
            i3 = subCont.rfind('\n')
            if i3 > 0:
                i2 = i+i3+1
            subCont = cont[i:i2]
            yield subCont
            i = i2


def next_str2(cont):
    i = 0
    L = len(cont)
    while i < L:
        print(1.0*i/L)
        i2 = cont.find('\n', i+100)
        if i2 > i+5000:
            i2 = i+5000

        subCont = cont[i:i2]

        yield subCont
        i = i2

translator = Translator()
foname = fname + '-cn.txt'
#cont = open(fname, errors='replace').read()
cont = open(fname, errors='ignore').read()
fdes = open(foname, 'w', encoding='utf-8')

for subCont in next_str2(cont):
    s = translator.translate(subCont, src='en', dest='zh-cn')
    try:
        fdes.write(subCont)
        fdes.write('\n')
        fdes.write(str(s.text))
        fdes.write('\n')
    except Exception as e:
        print('except:', e)
        
fdes.close()
