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

    #open csv
    filename = "scraperresults.csv"
    f = open(filename, "w")
    headers = "Title, NCT\n"
    f.write(headers)

    #find elements
    main_container = page_soup.findAll("div", {"id":"main-content"})
    title = main_container[0].h1.text

    date_container = page_soup.findAll("div",{"class":"w3-col m5"})
    nct = date_container[0].table.tr.td

    print(nct)

    #Add to csv
    # f.write(title.replace(",", "|") +","+ nct + "\n")