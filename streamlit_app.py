import streamlit as st
import os, sys
import time

os.system('sbase install geckodriver')
os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')


from selenium import webdriver
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)


browser.get('https://x.com/i/flow/login/')
time.sleep(7)
username = browser.find_element("name", "text")
username.click()
st.text("i am okkkk")
st.write(browser.page_source)
