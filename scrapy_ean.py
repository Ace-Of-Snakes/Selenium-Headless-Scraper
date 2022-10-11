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

#used for standard options
def getOptions():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    #user_ agent is used to simulate a non-headless browser, to avoid access denial
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=1')
    options.add_argument("--disable-3d-apis")
    return options

#startSession() is used to keep the browser open through global 
def startSession():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=getOptions())
    #initializes the user agent
    driver.execute_script("return navigator.userAgent")
    return driver

def scrape_ean(ean):
    try:
        #searchesthe eans
        driver.get(f'{"https://de.camelcamelcamel.com/search?sq="}{ean}')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,\
            '//*[@id="content"]/div[2]/div[3]/div[1]/div/p/span')))
        #goes into xpath with price and returns text value
        return driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[3]/div[1]/div/p/span').text
    except Exception:
        return ""

def iterate(pandas_df):
    startSession()
    for i in range(len(pandas_df)):
        pandas_df.loc[i,"Amazon-Preis"] = (scrape_ean(str(pandas_df.loc[i,"EAN-Code"])))[:-1]
        print(pandas_df.loc[i,"Amazon-Preis"])
        time.sleep(4)
    driver.quit()
