#adblock library
#functionality: none
from selenium import webdriver
import webbrowser

#getting to the adblockplus site
driver = webdriver.Chrome()
driver.get("chrome-extension://cfhdojbkjhnklbpkdaibdccddilifddb/options.html")

print("check 1")

#clicking the buttons
chrome-extensions
element_1 = driver.find_element_by_id('chrome-extension://cfhdojbkjhnklbpkdaibdccddilifddb/desktop-options.html#advanced')
element_1.click('''<input placeholder="Search or add filter(s) (e.g. /ads/track/*)">''')

print("check 2")
