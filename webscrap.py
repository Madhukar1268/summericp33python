from bs4 import BeautifulSoup # import the packages
import urllib.request
import os     # import os

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India" #define the url for web scraping
source_code = urllib.request.urlopen(url) #request the url with url using url lib
plain_text = source_code          #assign the value
soup = BeautifulSoup(plain_text, "html.parser")  #call the beautifulsoup method for passing the wiki page html page
print("Title is: ",soup.title.string) #print the title of the page
results = soup.find_all('a') #find the hyper links of the wiki hjtml page
print("Links are: ")
for link in results:  #loop each type of link
    print(link.get('href'))  #print the link values
rt_tab=soup.find('table', class_='wikitable sortable plainrowheaders') #find the table from the wiki page
print(rt_tab) #print the tab