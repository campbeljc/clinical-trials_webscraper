# clinical-trials_webscraper

## Purpose:

Scrapes [ClinicalTrials.gov](https://clinicaltrials.gov/) for important clinical trial information on selected disease or drug. 

With the rapidly expanding biotech and pharmaceutical industries, the number of clinical trials and drug candidates has grown exponentially. This increase has made background and competitive research more challenging and time consuming. This webscraper allows for the succinct aggregation of all data pertaining to a specified drug or disease.

The scraper exceeds the simple download option that clinicaltrials.gov provides because it allows for the collection of information that is not present on the summary search page.


## Function:

The webscraper first asks for a search term. This term is the same term you would put into the "Condition or disease" searchbox.

The scraper will then return a csv file that contains the following information about each clinical trial related to the disease:

1. Title
2. NCT Number
3. Phase Number
4. Start Date
5. End Date
6. Status
7. Number of Participants
8. Sponsor
9. Primary Endpoints
10. Secondary Endpoints
11. Drug of Interest

The csv file is saved to the same folder the program is run from.

## Using the Webscraper

To run the webscraper you will need the following packages installed:

* numpy
* selenium
* time
* bs4
* urllib
* os
* [Chrome Driver](https://chromedriver.chromium.org/)


To call the function simply type the following:
```
python3 webscraper.py
```

The program will ask you for a search term. You may input either a disease or drug. Make sure you check your spelling!

All results from the search will be scraped for the metrics described above, and stored in a csv file. The file is saved to a directory called "Results" that is saved to the same direcory the script is run from.
