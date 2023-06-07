import pytest
from selenium.webdriver.common.by import By
import time
from login import user, passw


link = 'https://stepik.org/lesson/236895/step/1'
def test_login(browser):
	browser.implicitly_wait(5)
	browser.get(link)
	browser.find_element(By.ID, 'ember33').click()
	browser.find_element(By.ID, 'id_login_email').send_keys(user)
	browser.find_element(By.ID, 'id_login_password').send_keys(passw)
	browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
	time.sleep(3)




