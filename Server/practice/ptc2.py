from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()

#ブラウザ立ち上げは処理が重たくなるので本番環境ではheadlessモードを採用
  # self.options.add_argument('--headless')

url = ('https://syllabus.kwansei.ac.jp/uniasv2/UnSSOLoginControlFree')
driver.get(url)



sleep(5)

driver.close()
driver.quit()
