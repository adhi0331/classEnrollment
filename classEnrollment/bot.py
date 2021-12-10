from webScraper import getCount, getURL, mainURL
from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Safari()
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        sleep(5)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(20)

InstaBot("adhi_ananthan", "Lamboaven03")


