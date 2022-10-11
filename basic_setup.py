#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
#some standard imports

#getOptions() function is used to set parameters for our CromeDriver
def getOptions():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    
    #____________________________________
    #The following options are here, so that the usual websites don#t detect us as a headless Browser, since many will try to block it
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))
    
    #____________________________________
    options.add_argument('--no-sandbox')
    
    #These following options vary from user to user dependant on the Errors, which the driver causes due to GUI
    options.add_argument('--log-level=1')
    options.add_argument("--disable-3d-apis")
    return options

#startSession() is used to keep the browser open through global methods 
#without using this the headless chrome browser will shortly open and close again, making ti impossible to scrape

def startSession():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=getOptions())
    #initializes the user agent, so we don't get blocked
    driver.execute_script("return navigator.userAgent")
    return driver
  
  if __name__ == "__main__":
    startSession()
    #your functions, loops, etc.
    driver.quit()
