from webScraper import getCount, getURL, mainURL
from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Safari()
        self.username = username
        self.pw = pw
    
    def login(self):
        self.driver.get("https://www.instagram.com")
        sleep(1)
        self.driver.find_element_by_name("username").click()
        self.driver.find_element_by_name("username").send_keys(self.username)
        sleep(1)
        for index,letter in enumerate(self.pw):
            self.driver.find_element_by_name("password").click()
            self.driver.find_element_by_name("password").send_keys(letter)
        sleep(1)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        #Maybe add a part to click on the save info button
    #A function that will read each new DM and return a list of all requests to be made
    def checkDM(self):
        sleep(2)
        self.driver.get("https://www.instagram.com/direct/inbox/")

        sleep(10)
    
    #Create a function that will iterate through the request list, ensures that each request is valid, if valid then run request

username = input("Enter username: ")
pw = input("Enter password: ")
stewie = InstaBot(username, pw)
stewie.login()
stewie.checkDM()
stewie.driver.close()


