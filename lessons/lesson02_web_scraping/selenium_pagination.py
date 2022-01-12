import time
from global_constants import browser
from bs4 import BeautifulSoup
import re

URL     = "https://bpl.bc.ca/events/"
browser.get(URL)

# Give the browser time to load all content.
time.sleep(1)
SEARCH_TERM = "Analytics"
search = browser.find_element_by_css_selector("input")
search.send_keys(SEARCH_TERM)

# Find the search button - this is only enabled when a search query is entered
button = browser.find_element_by_css_selector("button")
button.click()  # Click the button.
time.sleep(3)

def getContent(content):
    textContent =content.get_attribute('innerHTML')

    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="lxml")
    rawString = soup.get_text().strip()

    # Remove hidden characters for tabs and new lines.
    rawString = re.sub(r"[\n\t]*", "", rawString)

    # Replace two or more consecutive empty spaces with '*'
    rawString = re.sub('[ ]{2,}', '*', rawString)
    return rawString

# content = browser.find_elements_by_css_selector(".cp-search-result-item-content")
pageNum = 1

for i in range(0, 9):

    titles  = browser.find_elements_by_css_selector(".title-content")
    formats = browser.find_elements_by_css_selector(".manifestation-item-format-info-wrap")

    NUM_ITEMS = len(titles)

    # This technique works only if counts of all scraped items match.
    if(len(titles)!=NUM_ITEMS or len(formats)!=NUM_ITEMS):
        print("**WARNING: Items scraped are misaligned because their counts differ")

    for j in range(0, NUM_ITEMS):
        title       = getContent(titles[j])
        mediaFormat = getContent(formats[j])
        print("Title: " + title)
        print("Media: " + mediaFormat)
        print("********")

    # Go to a new page.
    pageNum += 1

    URL_NEXT = "https://burnaby.bibliocommons.com/v2/search?query=" \
               + SEARCH_TERM + "&searchType=smart&pagination_page="

    URL_NEXT = URL_NEXT + str(pageNum)
    browser.get(URL_NEXT)
    print("Count: ", str(i))
    time.sleep(3)

browser.quit()
print("done loop")
