import time
from global_constants import get_browser
from bs4 import BeautifulSoup
import re

# SEARCH JOB FAIRS
from selenium.webdriver.common.by import By

URL     = "https://www.eventbrite.ca/d/canada--vancouver/job-fair/"
browser = get_browser()
browser.get(URL)

# Give the browser time to load all content.
time.sleep(1)



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

    titles = browser.find_elements(By.XPATH, "//div[@data-spec='event-card__formatted-name--content']")
    dates = browser.find_elements(By.CSS_SELECTOR, ".eds-event-card-content__sub-title")
    NUM_ITEMS = len(titles)

    # This technique works only if counts of all scraped items match.
    if(len(titles)!=NUM_ITEMS or len(dates)!=NUM_ITEMS):
        print("**WARNING: Items scraped are misaligned because their counts differ")

    for j in range(0, NUM_ITEMS):
        title       = getContent(titles[j])
        date = getContent(dates[j])
        print("Title: " + title)
        print("Date: " + date)
        print("********")

    # Go to a new page.
    pageNum += 1

    URL_NEXT = "https://www.eventbrite.ca/d/canada--vancouver/job-fair/?page="

    URL_NEXT = URL_NEXT + str(pageNum)
    browser.get(URL_NEXT)
    print("Count: ", str(i))
    time.sleep(3)

browser.quit()
print("done loop")
