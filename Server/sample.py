from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver.common.keys import Keys
#ActionChainsを使う時は、下記のようにActionChainsのクラスをロードする
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup, BeautifulStoneSoup
from selenium.webdriver.chrome.options import Options
import requests
import json

# mac環境用
import chromedriver_binary

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore




class Syllabus:
    #初期化処理
    def __init__(self):
        self.options = Options()
        #ブラウザ立ち上げは処理が重たくなるので本番環境ではheadlessモードを採用
        # self.options.add_argument('--headless')
        self.options.add_argument('--window-size=1920,1080')
        #mac環境用
        self.driver = webdriver.Chrome(chrome_options=self.options)

        # Use a service account（Firebase）
        cred = credentials.Certificate('serviceAccount.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def act(self,url,value):
        self.driver.get(url)

        for i in range(1,15):
            print(f'スターーーーと{i}番目')
            #学部
            department = self.driver.find_element_by_id("selLsnMngPostCd")
            select = Select(department)
            department = select.options
            select.select_by_value(value)
            print(f'{department[i].text}スタート！！')

            # 検索ボタンをクリック
            self.driver.find_element_by_xpath('//*[@id="contents"]/div[2]/input[1]').click()
            
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
                administrativedepartment = self.driver.find_element_by_name('lblAc119ScrDispNm').get_attribute("value")
                coursenumber = self.driver.find_element_by_name('lblRepSbjKnjNm').get_attribute("value")
                instructor = self.driver.find_element_by_name('lstChagTch_st[0].lblTchName').get_attribute("value")
                dayandperiod = self.driver.find_element_by_name('lstSlbtchinftJ002List_st[0].lblTmtxCd').get_attribute("value")
              
                print(i)
                print(classcode)
                print(administrativedepartment)
                print(coursenumber)
                print(instructor)


                doc_ref = self.db.collection('subject')
                doc_ref.document(f'{department[i].text}').collection((num)).document().set({
                    '授業コード': classcode,
                    '管理部署': administrativedepartment,
                    '科目': coursenumber,
                    '担当教授': instructor,
                    '曜時': dayandperiod
                })


                # jsonに格納
                classinfo.setdefault(classcode, { 
                    '管理部署': administrativedepartment,
                    '科目': coursenumber,
                    '担当教授': instructor,
                    '曜時': dayandperiod,
                })        
                print(f'{classinfo}')

                # ページをスクロールして戻るボタンをクリック
                sleep(1)
                self.driver.find_element_by_tag_name('body').click()
                self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  
                sleep(1)

                self.driver.find_element_by_xpath('//*[@id="contents"]/div[2]/input').click()
            
            #戻るボタンクリック
            self.driver.find_element_by_xpath('//*[@id="contents"]/div[2]/input').click()

        # 処理が終わったらwindowを閉じる
        self.driver.close()
        self.driver.quit()
if __name__ == '__main__':
    driver = Syllabus()
    driver.act('https://syllabus.kwansei.ac.jp/uniasv2/UnSSOLoginControlFree',"21")