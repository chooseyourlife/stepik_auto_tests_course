from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import pyperclip


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)

if WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100')):
	browser.find_element(By.CSS_SELECTOR, '#book').click()

x = browser.find_element(By.ID, 'input_value').text

browser.find_element(By.ID, 'answer').send_keys(calc(x))
browser.find_element(By.ID, 'solve').click()

# Копирование числа из алерта в буфер обмена
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)


