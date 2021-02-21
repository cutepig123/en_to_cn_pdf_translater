from lib.mygoogletrans import Translator
import sys
import logging, coloredlogs

coloredlogs.install()
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
#print = lambda *tup : logging.info(str(" ".join([str(x) for x in tup]))) 

logging.info('from logging')
logging.error('error from logging')

translator = Translator()

subCont = 'hello'
s = translator.translate(subCont, src='en', dest='zh-cn')
print('translated', str(s.text))

