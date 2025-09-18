from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time 

driver = webdriver.Firefox()
url  = "https://demo.automationtesting.in/Register.html"
driver.get(url)

time.sleep(3)

action = ActionChains(driver)                   

hover_element = driver.find_element(By.XPATH,"//a[normalize-space()='SwitchTo']")

action.move_to_element(hover_element).perform()
time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='Frames']").click()

time.sleep(2)
driver.quit()
