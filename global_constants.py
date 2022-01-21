from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

PATH = "C:/Users/shagu/Documents/CST_T04/COMP_4949_BIG_DATA/data_sets/"
CHROMEDRIVER_PATH = "C:/Users/shagu/Downloads/chromedriver_win32/chromedriver.exe"


def get_browser():
    return webdriver.Chrome(ChromeDriverManager().install())