
from os import times
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")

driver.get('https://instagram.com/login')
driver.maximize_window()
time.sleep(5)
u_name = driver.find_element(By.NAME , "username")

u_name.send_keys("Enter your username here")
u_name.send_keys(Keys.RETURN)

time.sleep(5)
pass_word = driver.find_element(By.NAME, "password")
pass_word.send_keys("Enter your password here")
pass_word.send_keys(Keys.RETURN)

time.sleep(20)
submit = driver.find_element(By.CLASS_NAME, "_acan _acap _acas")
submit.send_keys(Keys.RETURN)
time.sleep(20)




















# driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")

# driver.get("https://www.instagram.com/")

# time.sleep(5)
# u_name = driver.find_element(By.NAME , "username")

# u_name.send_keys("anip.exe")
# u_name.send_keys(Keys.RETURN)

# time.sleep(5)
# pass_word = driver.find_element(By.NAME, "password")
# pass_word.send_keys("aniruddh6170")
# pass_word.send_keys(Keys.RETURN)