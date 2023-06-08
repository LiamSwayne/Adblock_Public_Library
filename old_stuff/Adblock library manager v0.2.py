#adblock library
#functionality: none
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")
element = driver.find_elements_by_xpath("//*[@type='submit']")
button = driver.find_element_by_id('<input placeholder="Search or add filter(s) (e.g. /ads/track/*)">')
print(element.get_attribute("class"))
driver.close()

print("check 1")

chrome-extensions
element_1 = driver.find_element_by_id('chrome-extension://cfhdojbkjhnklbpkdaibdccddilifddb/desktop-options.html#advanced')
element_1.click('''<input placeholder="Search or add filter(s) (e.g. /ads/track/*)">''')

'''
chrome-extension://cfhdojbkjhnklbpkdaibdccddilifddb/options.html
'''
