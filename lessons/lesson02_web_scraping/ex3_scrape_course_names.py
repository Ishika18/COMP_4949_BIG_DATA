import time
from global_constants import browser
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

URL = "https://www.bcit.ca/study/programs/5512cert#courses"

browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)


content = browser.find_elements(By.CSS_SELECTOR, ".course_name")

for e in content:
    start = e.get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features="lxml")
    print(soup.get_text())
    print("***")  # Go to new line.
