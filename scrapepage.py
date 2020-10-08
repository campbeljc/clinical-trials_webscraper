from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

#Url to Use for Testing
my_url = "https://clinicaltrials.gov/ct2/show/NCT00574613?cond=Dermal+Fibrosis&draw=2&rank=1"

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

    #NCT Number
    date_container = page_soup.findAll("div",{"class":"w3-col m5"})
    nct = date_container[0].table.tr.td.text
    nct = nct[-11:]

    #Start Date
    study_design = page_soup.findAll("table", {"class":"tr-studyInfo"})
    table_len = len(study_design[0].tbody.findAll("tr"))
  
    try:
        start = study_design[0].tbody.findAll("tr")[table_len-3].findAll("td")[1].text
        if len(start) > 20:
            start = ""
    except:
        start = ""

    #End Date
    try:
        end = study_design[0].tbody.findAll("tr")[table_len-2].findAll("td")[1].text
        if len(end) > 20:
            end = ""
    except:
        end = ""

    #Number of Participants
    try:
        participants = study_design[0].tbody.findAll("tr")[1].findAll("td")[1].text
        if len(participants) > 20:
            participants = ""
    except:
        participants = ""

    #Sponsor
    try:
        sponsor = page_soup.findAll("div", {"class":"tr-info-text"})[0].text
    except:
        sponsor = ""

    #Trial Status
    try:
        status_text = page_soup.findAll("div", {"class":"tr-status"})[0].text
        status = status_text.split("First Posted")[0].split(":")[1].strip()
        if "\n" in status:
            status  = "Unknown"
    except:
        status = ""

    #Phase
    try:
        phase = page_soup.findAll("td",{"class":"ct-body3"})[2].span.text
    except:
        phase =""

    #Primary Endpoints
    try:
        primary = page_soup.findAll("div",{"class":"tr-indent3"})[0].div.ol.findAll("li")
        primary_list = ""

        i = 0
        while i < len(primary):
            ptext = primary[i].find(text=True, recursive=False)
            pre_TF = ptext.find("[")
            post_TF = ptext.find("]")
            ptext = ptext[:pre_TF] + ptext[post_TF+1:]
            primary_list = primary_list + "   {index}) ".format(index = i+1) + ptext
            i += 1
    except: 
        primary_list=""

    #Secondary Endpoints
    try: 
        secondary = page_soup.findAll("div",{"class":"tr-indent3"})[0].findAll("div",{"class","ct-body3"})[1].ol.findAll("li")
        secondary_list = ""

        i = 0
        while i < len(secondary):
            stext = secondary[i].find(text=True, recursive=False)
            pre_TF = stext.find("[")
            post_TF = stext.find("]")
            stext = stext[:pre_TF] + stext[post_TF+1:]
            secondary_list = secondary_list + "   {index}) ".format(index = i+1) + stext
            i += 1
    except:
        secondary_list = ""


    return title, nct, start, end, participants, sponsor, status, phase, primary_list, secondary_list

# scrape_page()