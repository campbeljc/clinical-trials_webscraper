from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = "https://clinicaltrials.gov/ct2/show/NCT03580291?cond=Lupus+Nephritis&draw=2&rank=1"

def scrape_page(url=my_url):

    #open connection to webpage and saving webpage as page_html
    uClient = urlopen(url)
    page_html = uClient.read()
    uClient.close()

    #parse html
    page_soup = soup(page_html, "html.parser")

    #find elements
    main_container = page_soup.findAll("div", {"id":"main-content"})
    title = main_container[0].h1.text

    date_container = page_soup.findAll("div",{"class":"w3-col m5"})
    nct = date_container[0].table.tr.td.text
    nct = nct[-11:]

    study_design = page_soup.findAll("table", {"class":"tr-studyInfo"})
    table_len = len(study_design[0].tbody.findAll("tr"))
  
    try:
        start = study_design[0].tbody.findAll("tr")[table_len-3].findAll("td")[1].text
        if len(start) > 20:
            start = ""
    except:
        start = ""

    try:
        end = study_design[0].tbody.findAll("tr")[table_len-2].findAll("td")[1].text
        if len(end) > 20:
            end = ""
    except:
        end = ""

    try:
        participants = study_design[0].tbody.findAll("tr")[1].findAll("td")[1].text
        if len(participants) > 20:
            participants = ""
    except:
        participants = ""


    try:
        sponsor = page_soup.findAll("div", {"class":"tr-info-text"})[0].text
    except:
        sponsor = ""

    try:
        status_text = page_soup.findAll("div", {"class":"tr-status"})[0].text
        status = status_text.split("First Posted")[0].split(":")[1].strip()
        if "\n" in status:
            status  = "Unknown"
    except:
        status = ""

    try:
        phase = page_soup.findAll("td",{"class":"ct-body3"})[2].span.text
    except:
        phase =""

    try:
        primary = page_soup.findAll("div",{"class":"tr-indent3"})[0].div.ol.findAll("li")
        primary_list = []

        i = 0
        while i < len(primary):
            primary_list.append(primary[i].text)
            i += 1
    except: 
        primary_list=""

    try: 
        secondary = page_soup.findAll("div",{"class":"tr-indent3"})[0].findAll("div",{"class","ct-body3"})[1].ol.findAll("li")
    
        secondary_list = []

        i = 0
        while i < len(secondary):
            secondary_list.append(secondary[i].text)
            i += 1
    except:
        secondary_list = ""

    return title, nct, start, end, participants, sponsor, status, phase, primary_list, secondary_list

scrape_page()