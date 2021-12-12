from webScraper import getCount, getURL, mainURL
from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Safari()
        self.username = username
        self.pw = pw
    
    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(1)
        self.driver.find_element_by_name("username").click()
        self.driver.find_element_by_name("username").send_keys(self.username)
        sleep(1)
        for index,letter in enumerate(self.pw):
            self.driver.find_element_by_name("password").click()
            self.driver.find_element_by_name("password").send_keys(letter)
        sleep(1)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)
        self.driver.close()

username = input("Enter username: ")
pw = input("Enter password: ")
steve = InstaBot(username, pw)
steve.login()


