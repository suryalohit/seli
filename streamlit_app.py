import streamlit as st
import os, sys
import time

os.system('sbase install geckodriver')
os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')
for x in range(3):
  st.text(x)
  time.sleep(1)

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

for v in range(3):
  st.text(v)
  time.sleep(1)


browser.get('https://x.com/i/flow/login/')
time.sleep(7)
username = browser.find_element("name", "text")
for u in range(3):
  st.text(u)
  time.sleep(1)
username.click()
st.text("i am okkkk")
st.write(browser.page_source)
