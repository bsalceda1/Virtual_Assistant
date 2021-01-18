import selenium
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver"


fb_username = ""
fb_password = ""

def openfb():
	driver = webdriver.Chrome(PATH)
	driver.get("https://www.facebook.com/")
	return driver

def input_user_pass(driver):
	username = driver.find_element_by_id("email")
	username.clear()
	username.send_keys(fb_username)
	password = driver.find_element_by_id("pass")
	password.clear()
	password.send_keys(fb_password)

def login(driver):
	login_btn = driver.find_element_by_id("u_0_b")
	login_btn.click()


