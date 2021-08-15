# Arthur Foy
# 2021
# Hack For Type Racer


from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

x = webdriver.Chrome(ChromeDriverManager().install())
x.get('https://play.typeracer.com/')

WebDriverWait(x, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Enter a Typing Race"))).click()

wait = WebDriverWait(x, 200)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.gameStatusLabel"), "The race is on! Type the text below:"))
string = ""
try: 
    z = x.find_element_by_xpath('//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]').text
    string += z
except:
  pass  
try:
    y = x.find_element_by_xpath('//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]').text
    if string == "I" and len(y) > 3:
       string += " " + y
    string += y
except:
    pass
try: 
    xx = x.find_element_by_xpath('//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]').text
    string += (" " + xx)
except:
    pass


x.implicitly_wait(0)
text = x.find_element_by_css_selector('input.txtInput')
for i in string:
    for j in i:
        text.send_keys(j)
