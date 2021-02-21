import os, sys, requests
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import logging

class Result:
    def __init__(self):
        self.text = ''

class Translator:
    def __init__(self):
        browser = webdriver.Chrome()
        browser.maximize_window()  # 最大化窗口
        
        self.browser = browser

        url = 'https://translate.google.com.hk/?hl=en&tab=rT&sl=en&tl=zh-CN&op=translate'
        browser.get(url)

    def __del__(self):
        self.browser.close()
        self.browser.quit()
        logging.info ('quited')
       
    def translate(self, content, src='', dest=''):
        logging.info ('translating %s', content)
        browser = self.browser
        
        wait = WebDriverWait(browser, 10)  # 等待加载10s

        logging.info('try get input element')
        input = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')))
        #time.sleep(3)
        
        logging.info('clear input element')
        input.clear()
        
        if 0:
            logging.info('send data to input element')
            input.send_keys(content)
        else:
            logging.info('send script to input element')
            browser.execute_script('''
                //var t = document.evaluate("//textarea", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                var t = arguments[1];
                t.focus();
                t.value=arguments[0];
                //var event = new CustomEvent('change');
                //t.dispatchEvent(event); // no effect
                //t.change(); // run error
                ''', content, input)
            input.send_keys(' \n')

        logging.info('sleep3s')
        time.sleep(3)
        
        logging.info('try get output element')
        output = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@class='J0lOec']")))
        # logging.info('sleep3s')
        # time.sleep(3)
        #output.clear()
        innerText = output.get_attribute("innerText")
        logging.info('output is  %s', innerText)
        
        result = Result()
        result.text = innerText
        return result
       
