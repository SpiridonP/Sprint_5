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