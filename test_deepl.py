# Make imports
import time
import clipboard
from selenium import webdriver

# Define text to translate
text_to_translate = 'This is a translation example for my article.'

# Start a Selenium driver
driver_path='../chromedriver'
#driver = webdriver.Chrome(driver_path)
driver = webdriver.Chrome()

# Reach the deepL website
deepl_url = 'https://www.deepl.com/fr/translator'
driver.get(deepl_url)

# Get thie inupt_area 
input_css = 'div.lmt__inner_textarea_container textarea'
input_area = driver.find_element_by_css_selector(input_css)

# Send the text
input_area.clear() 
input_area.send_keys(text_to_translate)

# Wait for translation to appear on the web page
time.sleep(3)

# Get copybutton and click on it
button_css = ' div.lmt__target_toolbar__copy button' 
button = driver.find_element_by_css_selector(button_css)
button.click()

# Get content from clipboard
content = clipboard.paste()

# Quit selenium driver
driver.quit()

# Display results
print('_'*50)
print('Original    :', text_to_translate)
print('Translation :', content)
print('_'*50)