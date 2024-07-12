import streamlit as st
from time import sleep

  
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
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    driver = get_driver()
    driver.get("https://www.cricbuzz.com/")
    liv=driver.find_element("xpath", '//*[@id="cb-main-menu"]/a[2]')
    st.text(liv.text)
    print(liv.text)
    for i in range(10):
        st.text(i)
        liv=driver.find_element("xpath", '//*[@id="cb-main-menu"]/a[2]')
        st.text(liv.text)
        
        sleep(1.5)

    st.code(driver.page_source)
