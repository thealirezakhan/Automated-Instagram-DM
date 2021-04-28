from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

username = ('Enter your username here')
password = ('Enter your password here')
url = 'https://www.instagram.com/' + input('Enter Username : ')

def path():
    global chrome

    chrome = webdriver.Chrome(executable_path='C:/ALI reza/chromedriver.exe')
def url_name(url):
    chrome.get(url)

    time.sleep(4)

def login(username, password):
	log_but = chrome.find_element_by_class_name("L3NKy") 
	time.sleep(2)
	log_but.click()
	time.sleep(4)
	
	# finds the username box 
	usern = chrome.find_element_by_name("username")
	
	# sends the entered username 
	usern.send_keys(username)

	# finds the password box 
	passw = chrome.find_element_by_name("password")

	# sends the entered password 
	passw.send_keys(password)
	
	# press enter after sending password
	passw.send_keys(Keys.RETURN) 
	time.sleep(5.5)
	
	# Finding Not Now button
	notk = chrome.find_element_by_class_name("yWX7d") 
	notk.click()
	time.sleep(3)

def send_message():

	# Find message button
	message = chrome.find_element_by_class_name('_862NM ') 
	message.click()
	time.sleep(2)
	chrome.find_element_by_class_name('HoLwm ').click()
	time.sleep(1)
	l = ['hey..This message is sent using python']
	for x in range(1):
		mbox = chrome.find_element_by_tag_name('textarea')
		mbox.send_keys(random.choice(l))
		mbox.send_keys(Keys.RETURN)
		time.sleep(1.2)

path()
time.sleep(1)
url_name(url)
login(username, password)
send_message()
chrome.close()

