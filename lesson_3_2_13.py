from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'

class TestRegistration(unittest.TestCase):
	def test_link1(self):
		browser = webdriver.Chrome()
		browser.get(link1)
		input_1 = browser.find_element(By.CSS_SELECTOR, ".form-group.first_class > [placeholder='Input your first name']")
		input_1.send_keys("Ivan")
		input_2 = browser.find_element(By.CSS_SELECTOR, ".form-group.second_class > [placeholder='Input your last name']")
		input_2.send_keys("Petrov")
		input_3 = browser.find_element(By.CSS_SELECTOR, ".form-group.third_class > [placeholder='Input your email']")
		input_3.send_keys("brodvey77@gmail.com")
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()

		welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


	def test_link2(self):
		browser = webdriver.Chrome()
		browser.get(link2)
		input_1 = browser.find_element(By.CSS_SELECTOR, ".form-group.first_class > [placeholder='Input your first name']")
		input_1.send_keys("Ivan")
		input_2 = browser.find_element(By.CSS_SELECTOR, ".form-group.second_class > [placeholder='Input your last name']")
		input_2.send_keys("Petrov")
		input_3 = browser.find_element(By.CSS_SELECTOR, ".form-group.third_class > [placeholder='Input your email']")
		input_3.send_keys("brodvey77@gmail.com")
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()

		welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text)



if __name__ == "__main__":
	unittest.main()