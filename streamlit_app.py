
import streamlit as st
from time import sleep
import threading

  
import requests
TOKEN = "6994416717:AAH_qEF1vSy1gZc1nXQ4eyM4dErJshFGJaM"
chat_id = "998041732"
message = "hello ra 2"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
requests.get(url).json()

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

    options = Options()
    options.add_argument("--headless")
    
    driver = get_driver()
   
    driver.get('https://x.com/i/flow/login/')
    sleep(10)
    st.text(driver.page_source)
    st.text("on login page")
   
    username = driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
    username.click()
    username.send_keys('retiredHippo')
    next=driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
    next.click()
    sleep(10)
    st.text("given username")


    password = driver.find_element("name", "password")
    password.click()
    password.send_keys('Asailohit30@')


    signin=driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
    signin.click()
    st.text("given password")

    sleep(10)

    for i in range(30):
        st.text(i)
        message = i
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url).json()

        message = threading.get_ident()
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url).json()

        driver.get('https://x.com/DaoKwonDo/')
        sleep(10)
        prof=driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/a')
        
        message = prof.get_attribute("href")
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url).json()
        
        
      
        st.text(liv.text)
        
        sleep(1.5)

    st.code(driver.page_source)


