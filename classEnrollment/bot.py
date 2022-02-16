from webScraper import getCount, getURL, mainURL
from selenium import webdriver
from time import sleep
from datetime import datetime
class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Safari()
        self.username = username
        self.pw = pw
        self.requestList = []
    
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
        sleep(2)
        #Maybe add a part to click on the save info button
    #A function that will read each new DM, check if the request is valid, and if valid add it to the dictionary
    def checkDM(self):
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        
        sleep(2) 
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a').click()
        
        sleep(2)
        messages = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div').text.lower()
        print(messages)
        messageList = messages.split("!") #Have to enter message in format !0ID00,0,00
        print(messageList)
        for message in messageList:
            if message == "stop":
                self.driver.close()
                return False
            if len(message) == 10:
                self.requestList.append(message)
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]').send_keys("confirmed")
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]').click()
                
        sleep(2) 
        return True

    #Create a function that returns the time of day
    def checkTime(self):
        now = datetime.now()
        currentHour = int(now.strftime("%H"))
        currentTime = int(now.strftime("%M"))
        return currentHour, currentTime 
    
    #the getCount and return count method here

    def returnCount(self):
        for request in self.requestList:
            components = request.split(',')
            count = getCount(mainURL, components[0])
            count.replace(" ", "")
            for index,letter in enumerate(count):
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]').send_keys(letter)
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]').click()
            
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]').click()
            self.requestList.remove(request)

        

#username = input("Enter username: ")
#pw = input("Enter password: ")
stewie = InstaBot("stewie_thefriend", "Stewie123")
stewie.login()
while (stewie.checkDM() == True):
    if len(stewie.requestList) >= 1:
        stewie.returnCount()
    



