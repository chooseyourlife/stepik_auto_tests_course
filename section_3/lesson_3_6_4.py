import pytest
from selenium.webdriver.common.by import By
import time
from login import user, passw

import time
import math


answer = ''

@pytest.mark.parametrize('links',[
	"https://stepik.org/lesson/236895/step/1", 
	"https://stepik.org/lesson/236896/step/1", 
	"https://stepik.org/lesson/236897/step/1", 
	"https://stepik.org/lesson/236898/step/1", 
	"https://stepik.org/lesson/236899/step/1", 
	"https://stepik.org/lesson/236903/step/1", 
	"https://stepik.org/lesson/236904/step/1", 
	"https://stepik.org/lesson/236905/step/1"])
def test_login(browser, links):
	browser.implicitly_wait(20)
	link = f'{links}'
	browser.get(link)
	browser.find_element(By.ID, 'ember33').click()
	browser.find_element(By.ID, 'id_login_email').send_keys(user)
	browser.find_element(By.ID, 'id_login_password').send_keys(passw)
	browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

	# поиск текстового поля для вставки ответа и отправка ответа на проверку
	browser.find_element(By.CSS_SELECTOR, '.ember-text-area').send_keys(math.log(int(time.time())))

	# нашимаем кнопку подтверждения
	browser.find_element(By.CLASS_NAME, 'submit-submission').click()

	word = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text

	assert word == 'Correct!', f'{answer} + {word}'







