import pytest
from selenium import webdriver
import settings

import random

def make_email():
  username = ""
  for i in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-._+":
    chance = random.random()
    if chance < 0.1:
      username += i
  domain = "ya.ru"
  email = username+"@"+domain
  return email
email = make_email()


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL)
    return chrome_driver


