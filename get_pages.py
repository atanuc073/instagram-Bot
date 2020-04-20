from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Getpages:
    def __init__(self,driver):
        self.driver=driver

    def get_followers(self):
        flw_btn=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/ul/li[2]/a/span')))
        flw_btn.click()
        popup=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div[2]")))
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',popup)