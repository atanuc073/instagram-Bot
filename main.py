from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import get_pages

username='atanuc73'
password='RYW6HrcjxfsDV34'



driver=0
def main():
    global driver
    print("Running script ..")
    driver=webdriver.Chrome('chromedriver_linux64/chromedriver')
    l=login.Login(driver,username,password)
    l.signin()
    driver.get('https://www.instagram.com/python.learning/')
    gp=get_pages.Getpages(driver)
    print(gp.get_num_flw())
    gp.get_followers()
    

if __name__ == "__main__":
    main()