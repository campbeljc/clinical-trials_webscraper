from selenium import webdriver
import time
import numpy as np
import sys
import os

from selenium.webdriver.support.ui import Select

from getlinks import get_links
from scrapepage import scrape_page

# Get Search Term
if True:
    search_term = input("Enter Search Term: ")
else:
    search_term = "Lupus Nephritis"

search_term = search_term.replace(" ","+")

#Get url of search result page
url = "https://clinicaltrials.gov/ct2/results?cond="+search_term+"&term=&cntry=&state=&city=&dist="

#Open Web Driver
try:
    driver = webdriver.Chrome("/Users/jennacampbell/Desktop/webscraper/chromedriver")
    driver.get(url)
except:
    driver.quit()
    exit("No search results. Please try a different search term.")

#Allow all results to load
time.sleep(2)

#Select 100 Results Visisble per page
try:
    selector = Select(driver.find_element_by_name("theDataTable_length"))
    selector.select_by_visible_text('100')
except:
    driver.quit()
    exit("No search results. Please try a different search term.")

#Collect all links
next_page = True
link_list = []
while next_page:
    link_list = get_links(driver, link_list)
    arrow = driver.find_elements_by_class_name("paginate_button")[2]
    last_page = arrow.get_attribute("class").find("disabled")
    if last_page != -1:
        next_page = False
    else:
        arrow.click()

driver.quit()

total_results = len(link_list)

print("{} trials found, scraping each page...".format(total_results))

#Create directory for results
parent_dir = os.getcwd()
dir_path = os.path.join(parent_dir, "Results") 

dir_exists = os.path.exists(dir_path)

if not dir_exists:
    os.mkdir(dir_path)

#Make CSV
search_term = search_term.replace("+","_")
filename = "Scraperresults_{term}.csv".format(term = search_term)
file_path = os.path.join(dir_path, filename)
f = open(file_path, "w")
headers = "Title, NCT, Start Date, End Date, Participants, Sponsor, Status, Phase, Primary Endpoints, Secondary Endpoints\n"
f.write(headers)

progress = 1

def csv_fix(text):
    text = text.replace(",","|").replace("\n","")
    return text

# Scrape each link
for page in link_list:
    print("scraping page "+str(progress))
    title, nct, start, end, participants, sponsor, status, phase, primary, secondary = scrape_page(page)
    progress +=1

#Add to csv
    f.write(csv_fix(title) +","+ csv_fix(nct) + "," + csv_fix(start) + "," + csv_fix(end) + "," + participants + "," + csv_fix(sponsor) + "," + csv_fix(status)+ "," + csv_fix(phase) + "," + csv_fix(primary) + "," + csv_fix(secondary) + "\n")


print("finished!")

f.close()