import streamlit as st
import os, sys


os.system('sbase install geckodriver')
os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')


from selenium import webdriver
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

browser.get('https://www.cricbuzz.com/')
ph=browser.find_element("xpath", '//*[@id="cb-main-menu"]/a[2]')
st.text(ph.text)
st.text("i am okkkk")
st.write(browser.page_source)
