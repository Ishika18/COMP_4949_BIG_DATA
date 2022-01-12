import time
from global_constants import browser
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

URL = "https://www.rottentomatoes.com/critics/latest_reviews"

browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)


content = browser.find_element(".critics-latest-reviews__data-review .a", By.CSS_SELECTOR)
for e in content:
    start = e.get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features="lxml")
    print(soup.get_text())
    print("***")  # Go to new line.
