from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome import options
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument('--headless')

driver = webdriver.Chrome(options = options) 

url = ('https://syllabus.kwansei.ac.jp/uniasv2/UnSSOLoginControlFree')
driver.get(url)

select_element = driver.find_element_by_id('selTacTrmCd')
select_object = Select(select_element)
select_object.select_by_value('02')

select_element = driver.find_element_by_id('selOpcCmpsCd')
select_object = Select(select_element)
select_object.select_by_value('1')

select_element = driver.find_element_by_id('selLsnMngPostCd')
select_object = Select(select_element)
select_object.select_by_value('21')

select_element = driver.find_element_by_id('selTmtxCd')
select_object = Select(select_element)
select_object.select_by_value('A1')



# sleep(5)

# driver.close()
# driver.quit()
