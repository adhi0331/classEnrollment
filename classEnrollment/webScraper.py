
import requests
import bs4

mainURL = "https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm?selectedTerm=SP22&tabNum=tabs-sec&sections="

#Create a function that gets the URL for the specific course
def getURL():
    return input("Enter course code: ")


#Create a function that returns waitlst/enrollment count for any URL
def getCount(URL,x):
    result = requests.get(URL+x)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    
    sectionTexts = soup.select(".sectxt") #Finds each tag with class=sectxt
    
    for section in sectionTexts:
        if section.contents[5].text.strip() == x: #Verify if class being examined is user input
           return(section.contents[21].text.strip()) #Return class enrollment
    







