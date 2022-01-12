from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = None

# This loads webdriver from the local machine if it exists.
try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    print("The path to webdriver_manager was found.")

# If a webdriver not found error occurs it is then downloaded.
except:
    print("webdriver not found. Update 'PATH' with file path in the download.")
