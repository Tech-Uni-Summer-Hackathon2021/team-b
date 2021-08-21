from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
#ActionChainsを使う時は、下記のようにActionChainsのクラスをロードする
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
#from bs4 import BeautifulSoup, BeautifulStoneSoup
from selenium.webdriver.chrome.options import Options

# mac環境用
import chromedriver_binary




class Test:
    #初期化処理
    def __init__(self):
        self.options = Options()
        #ブラウザ立ち上げは処理が重たくなるので本番環境ではheadlessモードを採用
        # self.options.add_argument('--headless')
        self.options.add_argument('--window-size=1920,1080')

        #Tsukasa環境用
        # self.driver = webdriver.Chrome('C:\work\chromedriver_win32\chromedriver')

        #Yusuke環境用
        self.driver = webdriver.Chrome(chrome_options=self.options)

    

    def act(self,url):
        self.driver.get(url)

        # 処理が終わったらwindowを閉じる
        #self.driver.close()
        #self.driver.quit()

        # return json
if __name__ == '__main__':
    driver = Test()
    driver.act('https://syllabus.kwansei.ac.jp/uniasv2/UnSSOLoginControlFree')


