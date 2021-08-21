from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome import options

from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument('--headless')

driver = webdriver.Chrome(options = options) 

url = ('https://syllabus.kwansei.ac.jp/uniasv2/UnSSOLoginControlFree')
driver.get(url)



sleep(5)

driver.close()
driver.quit()
