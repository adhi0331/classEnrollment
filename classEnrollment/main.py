
import requests
import bs4

#Create a function that gets the URL for the specific course
def getURL():
    return None


#Create a function that returns waitlst/enrollment count for any URL
def getCount(URL):
    result = requests.get(URL)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    for item in soup:
        print(type(item))

    siteTables = soup.select(".ertext")
    print(siteTables[3].text)

getCount("https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm?selectedTerm=WI22&tabNum=tabs-sec&sections=66040")
print("Hello")
#"https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm?selectedTerm=WI22&tabNum=tabs-sec&sections=66040"
#45
