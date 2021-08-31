from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
#ActionChainsを使う時は、下記のようにActionChainsのクラスをロードする
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup, BeautifulStoneSoup
from selenium.webdriver.chrome.options import Options
import requests
import json


# mac環境用
#import chromedriver_binary




class Syllabus:
    #初期化処理
    def __init__(self):
        self.options = Options()
        #ブラウザ立ち上げは処理が重たくなるので本番環境ではheadlessモードを採用
        #self.options.add_argument('--headless')
        self.options.add_argument('--window-size=1920,1080')

        #windows環境用
        # self.driver = webdriver.Chrome('C:\work\chromedriver_win32\chromedriver')

        #mac環境用
        self.driver = webdriver.Chrome('/Users/tsukasa/Downloads/chromedriver 2')

    def act(self,url,value):
        self.driver.get(url)

        for i in range(1,16):

            #学部
            department = self.driver.find_element_by_id('selLsnMngPostCd')
            select = Select(department)
            department = select.options
            select.select_by_value(value)
            print(f'{department[i].text}')

            #検索ボタンをクリック
            self.driver.find_element_by_name('ESearch').click()

             # 科目一覧のソースコード取得
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            # 詳細見るためのボタンをクリック
            class_lists = soup.find_all("tr")[1:]
            max_num = len(class_lists)

            # 授業格納Object
            classinfo = {}
            self.driver.find_element_by_name
            
            for num in range(2,max_num+1):
                sleep(1)
                self.driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[2]/table/tbody/tr[{num}]/td[1]/input[1]').click()

                classcode = self.driver.find_element_by_name('lblLsnCd').get_attribute("value")
                campus = self.driver.find_element_by_name('lblCc019ScrDispNm').get_attribute("value")
                administrativedepartment = self.driver.find_element_by_name('lblAc119ScrDispNm').get_attribute("value")
                term_offered = self.driver.find_element_by_name('lstSlbtchinftJ002List_st[0].lblAc201ScrDispNm_02').get_attribute("value")
                coursenumber = self.driver.find_element_by_name('lblRepSbjKnjNm').get_attribute("value")
                dayandperiod = self.driver.find_element_by_name('lstSlbtchinftJ002List_st[0].lblTmtxCd').get_attribute("value")
              
                print(i)
                print(classcode)
                print(campus)
                print(administrativedepartment)
                print(term_offered)
                print(coursenumber)
                print(dayandperiod)


                # jsonに格納
                classinfo.setdefault(classcode, { 
                    '開講キャンパス': campus,
                    '学部': administrativedepartment,
                    '科目': coursenumber,
                    '学期': term_offered,
                    '曜日': dayandperiod,
                })        
                print(f'{classinfo}')

                # ページをスクロールして戻るボタンをクリック
                sleep(1)
                self.driver.find_element_by_tag_name('body').click()
                self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  
                sleep(1)

                self.driver.find_element_by_xpath('//*[@id="contents"]/div[2]/input').click()

                
            if self.driver.find_element_by_name('ESearch').click():
                self.driver.find_element_by_name('ESearch').click()

                

                



            
            #戻るボタンクリック
            self.driver.find_element_by_xpath('//*[@id="contents"]/div[2]/input').click()






        # 処理が終わったらwindowを閉じる 
        #self.driver.close()
        #self.driver.quit()


        # return json
if __name__ == '__main__':
    driver = Syllabus()
    driver.act('https://syllabus.kwansei.ac.jp/uniasv2/UnSSOLoginControlFree',"21")