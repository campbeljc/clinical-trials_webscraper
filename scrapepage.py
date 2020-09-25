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

    study_design = page_soup.findAll("table", {"class":"ct-layout_table"})
    start = study_design[0].tbody.findAll("tr")[7].findAll("td")[1].text

    end = study_design[0].tbody.findAll("tr")[8].findAll("td")[1].text

    participants = study_design[0].tbody.findAll("tr")[1].findAll("td")[1].text

    sponsor = page_soup.findAll("div", {"class":"tr-info-text"})[0].text

    status_text = page_soup.findAll("div", {"class":"tr-status"})[0].text
    status = status_text.split("First Posted")[0].split(":")[1].strip()

    phase = page_soup.findAll("td",{"class":"ct-body3"})[2].span.text

    primary = page_soup.findAll("div",{"class":"tr-indent3"})[0].div.ol.findAll("li")
    primary_list = []

    i = 0
    while i < len(primary):
        primary_list.append(primary[i].text)
        i += 1

    secondary = page_soup.findAll("div",{"class":"tr-indent3"})[0].findAll("div",{"class","ct-body3"})[1].ol.findAll("li")
 
    secondary_list = []

    i = 0
    while i < len(secondary):
        secondary_list.append(secondary[i].text)
        i += 1

    return title, nct, start, end, participants, sponsor, status, phase, primary, secondary
