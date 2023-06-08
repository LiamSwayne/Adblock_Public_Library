#adblock library
#functionality: none
#attempt 3 from scratch
'''
#imports
import time
from selenium import webdriver
 
driver = webdriver.Chrome()
 
#URL of website
url = "https://www.geeksforgeeks.org/"
 
#Opening the website
driver.get(url)
 
#getting the button by class name
button = driver.find_element_by_class_name("slide-out-btn")
 
#clicking on the button
button.click()
'''

#attempt 4 from scratch
'''
from selenium import webdriver
print("check")
#set chromodriver path
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
print("check")
#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://www.tutorialspoint.com/index.htm")
#identify element
l =driver.find_element_by_xpath("//button[text()='Check it Now']")
#perform click
l.click()
print("Page title is: ")
print(driver.title)
#close browser
driver.quit()
'''

#attempt 5 from scratch
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
 
#--| Setup
options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
browser = webdriver.Chrome(executable_path=r'C:\cmder\bin\chromedriver.exe', options=options)
#--| Parse or automation
browser.get('https://www.morningstar.com/stocks/XOSL/XXL/quote.html')
time.sleep(1)
soup = BeautifulSoup(browser.page_source, 'lxml')
price_sales = soup.select('li:nth-child(9) > div > div.dp-value.ng-binding')
print(price_sales[0].text.strip())
