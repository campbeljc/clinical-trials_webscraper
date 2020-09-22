from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
# from selenium import webdriver

if False:
    search_term = input("Enter Search Term: ")
else:
    search_term = "Lupus Nephritis"

search_term = search_term.replace(" ","+")

url = "https://clinicaltrials.gov/ct2/results?cond="+search_term+"&term=&cntry=&state=&city=&dist="

# d = webdriver.Chrome()
# d.get(url)

uClient = urlopen(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "lxml")

table = page_soup.find("table",{"id":"theDataTable"})

odd_rows = table.findAll("tr",{"class": "odd"})

print(len(odd_rows))

#click on buttons
# link = html_element
# link.click()

# driver.back()

# f.close()