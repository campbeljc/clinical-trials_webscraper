from selenium import webdriver
import time
import numpy as np

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Get Search Term
if False:
    search_term = input("Enter Search Term: ")
else:
    search_term = "Lupus Nephritis"


search_term = search_term.replace(" ","+")

url = "https://clinicaltrials.gov/ct2/results?cond="+search_term+"&term=&cntry=&state=&city=&dist="

driver = webdriver.Chrome("/Users/jennacampbell/Desktop/webscraper/chromedriver")
driver.get(url)

time.sleep(5)

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

print(link_list)

driver.quit()

print("all links found, scraping each page")

#Scrape each link
from scrapepage import scrape_page

#Make CSV
filename = "scraperresults.csv"
    f = open(filename, "w")
    headers = "Title, NCT\n"
    f.write(headers)
    f.close()

for page in link_list:
    title, nct, start, end, participants, sponsor, status, phase, primary, secondary = scrape_page(page)

    #Add to csv
    f.open(filename,"a")
    f.write(title.replace(",", "|") +","+ nct + "\n")

f.close()

# try:
#     table = WebDriverWait(driver,10).until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, "parent"))
#     )
#     print("table loaded...")

#     for row in table:
#         cells = row.find_elements_by_tag_name("td")
#         link = cells[3].find_element_by_tag_name("a").get_attribute("href")
#         print(link)

# finally:
#     driver.quit()