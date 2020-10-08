
import time

def get_links(driver,link_list):
    #Allow all 100 results to load
    time.sleep(2)

    #Retrieve links for all pages found by search result
    table = driver.find_element_by_id("theDataTable")
    rows = table.find_elements_by_tag_name("tr")
    rows = rows[1:]

    for row in rows:
        cells = row.find_elements_by_tag_name("td")
        link_cell = cells[3]
        link = link_cell.find_elements_by_tag_name("a")
        href = link[0].get_attribute("href")
        link_list.append(href)
    
    return link_list