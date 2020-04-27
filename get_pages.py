from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Getpages:
    def __init__(self,driver):
        self.driver=driver
        self.driver.get("https://www.instagram.com/python.learning/followers/")
        # 12 pages per loading

    def get_num_flw(self):
        flw=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#react-root > section > main')))
        sflw=b(flw.get_attribute('innerHTML'),'html.parser')
        
        followers=sflw.findAll('span',{'class':'g47SY'})
        f=followers[1].getText().replace(',','')

        if 'k' in f:
            f=float(f[:-1])*10**3
            return f
        elif 'm' in f:
            f=float(f[:-1])*10**3
            return f
        else:
            return float(f)




    def get_followers(self):
        
        flw_btn=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/ul/li[2]/a/span')))
        flw_btn.click()
        popup=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div[2]")))
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',popup)