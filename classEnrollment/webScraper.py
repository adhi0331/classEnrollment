
import requests
import bs4

#Create a function that gets the URL for the specific course
def getURL():
    return input("Enter course code: ")


#Create a function that returns waitlst/enrollment count for any URL
def getCount(URL,x):
    result = requests.get(URL+x)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    
    sectionTexts = soup.select(".sectxt")
    
    for section in sectionTexts:
        if section.contents[5].text.strip() == x:
           print(section.contents[21].text.strip()) 
    

x = getURL()
getCount("https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm?selectedTerm=WI22&tabNum=tabs-sec&sections=",x)


