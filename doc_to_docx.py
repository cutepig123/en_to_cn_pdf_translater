from win32com import client as wc #导入模块
import os, sys

#https://zhuanlan.zhihu.com/p/64189783
class WordProcessor:
    def __init__(self):
        self._word = None

    def __del__(self):
        word = self._word
        if word:
            word.Quit()

    def to_docx(self, file):
        word = self._word
        if not word:
            word = wc.DispatchEx("Word.Application") # 打开word应用程序
            #word = wc.gencache.EnsureDispatch('Word.Application')
            word.Visible = True
            self._word = word

        doc = word.Documents.Open(file) #打开word文件
        doc.SaveAs("{}x".format(file), 12)#另存为后缀为".docx"的文件，其中参数12指docx文件
        doc.Close() #关闭原来word文件
    #word.Quit()

path=sys.argv[1]
#path=r'C:\Users\aeejshe\Documents\doc'
g_WordProcessor = WordProcessor()
for file in os.listdir(path):
    docxFile = '{}x'.format(file)
    if file.lower().endswith('.doc') and not os.path.isfile(docxFile):
        print(file)
        g_WordProcessor.to_docx('%s\\%s'%(path,file))
