from selenium import webdriver
import time
import numpy as np
import sys

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Get Search Term
if True:
    search_term = input("Enter Search Term: ")
else:
    search_term = "Lupus Nephritis"


search_term = search_term.replace(" ","+")

url = "https://clinicaltrials.gov/ct2/results?cond="+search_term+"&term=&cntry=&state=&city=&dist="

try:
    driver = webdriver.Chrome("/Users/jennacampbell/Desktop/webscraper/chromedriver")
    driver.get(url)
except:
    driver.quit()
    exit("No search results. Please try a different search term.")

time.sleep(2)

try:
    selector = Select(driver.find_element_by_name("theDataTable_length"))
    selector.select_by_visible_text('100')
except:
    driver.quit()
    exit("No search results. Please try a different search term.")


time.sleep(3)


table = driver.find_element_by_id("theDataTable")
rows = table.find_elements_by_tag_name("tr")
rows = rows[1:]

link_list = []

for row in rows:
    cells = row.find_elements_by_tag_name("td")
    link_cell = cells[3]
    link = link_cell.find_elements_by_tag_name("a")
    href = link[0].get_attribute("href")
    link_list.append(href)

driver.quit()

print("all trials found, scraping each page")

#Scrape each link
from scrapepage import scrape_page

#Make CSV
search_term = search_term.replace("+","_")
filename = "Scraperresults_{term}.csv".format(term = search_term)
f = open(filename, "w")
headers = "Title, NCT, Start Date, End Date, Participants, Sponsor, Status, Phase, Primary Endpoints, Secondary Endpoints\n"
f.write(headers)

progress = 1
for page in link_list:
    print("scraping page "+str(progress))
    title, nct, start, end, participants, sponsor, status, phase, primary, secondary = scrape_page(page)
    progress +=1

#Add to csv
    f.write(title.replace(",", "|").replace("\n","") +","+ nct.replace("\n","") + "," + start.replace(",", "|").replace("\n","") + "," + end.replace(",", "|").replace("\n","") + "," + participants + "," + sponsor.replace(",","|").replace("\n","") + "," + status.replace(",","|").replace("\n","")+ "," + phase.replace("\n","") + "\n")

print("finished!")

f.close()