from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:/Users/Светлана/Downloads/chromedriver_win32/chromedriver.exe')
driver: WebDriver = webdriver.Chrome(service=s)

driver.get("https://qahacking.guru/")
driver.set_window_size(1248, 654)
driver.find_element(By.CSS_SELECTOR, ".uk-navbar-nav > li:nth-child(1) > a").click()
driver.find_element(By.ID, "firstName").click()
driver.find_element(By.ID, "firstName").send_keys("sv")
driver.find_element(By.ID, "lastName").click()
driver.find_element(By.ID, "lastName").send_keys("sv")
driver.find_element(By.ID, "userEmail").click()
driver.find_element(By.ID, "userEmail").send_keys("svbnm@mail.ru")
driver.find_element(By.ID, "sex-1").click()
driver.find_element(By.ID, "userNumber").click()
driver.find_element(By.ID, "userNumber").send_keys("123456789")
driver.find_element(By.ID, "date").click()
driver.find_element(By.ID, "date").send_keys("12.12.1233")
driver.find_element(By.ID, "hobbies-checkbox-1").click()
driver.find_element(By.ID, "hobbies-checkbox-2").click()
driver.find_element(By.CSS_SELECTOR, ".col-md-9:nth-child(6) #hobbies-checkbox-1").click()
driver.find_element(By.ID, "currentAddress").click()
driver.find_element(By.ID, "currentAddress").send_keys("test")
driver.find_element(By.ID, "submit").click()
  
