import requests
from bs4 import BeautifulSoup

#creating class to get the url
def getdata(url):
    r = requests.get(url)
    return r.text
#creating object and parser to find the top 5

htmldata = getdata("https://covid-19tracker.milkeninstitute.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
result = str(soup.find_all("div", class_="is_h5-2 is_developer w-richtext"))

#printing the result with selecting the text
print("NO 1 " + result[48:125])
print("NO 2 " + result[178:219])
print("NO 3 " + result[271:320])
print("NO 4 " + result[411:436])
print("NO 5 " + result[490:505])