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

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# mac環境用
#import chromedriver_binary


class Syllabus:
    #初期化処理
    def __init__(self):
        self.options = Options()
        #ブラウザ立ち上げは処理が重たくなるので本番環境ではheadlessモードを採用
        self.options.add_argument('--headless')
        self.options.add_argument('--window-size=1920,1080')

        #windows環境用
        # self.driver = webdriver.Chrome('C:\work\chromedriver_win32\chromedriver')

        #tsukasa環境用
        self.driver = webdriver.Chrome('/Users/tsukasa/Downloads/chromedriver 2')

        # Use a service account（Firebase）
        cred = credentials.Certificate('serviceAccount.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def act(self,url,value):
        self.driver.get(url)

        for i in range(1,8):
          
          x = 2
          #開講キャンパス
          Campus = self.driver.find_element_by_id('selOpcCmpsCd')
          select = Select(Campus)
          department = select.options
          select.select_by_value(str(x))

          #全てのキャンパス情報を取得
          #select.select_by_value(str(i))


          # print(f'{department[2].text}')


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


          for i in range(100):
            print('始まり')
            for num in range(2,max_num+2):
                    sleep(1)
                    self.driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[2]/table/tbody/tr[{num}]/td[1]/input[1]').click()

                    classcode = self.driver.find_element_by_name('lblLsnCd').get_attribute("value")
                    campus = self.driver.find_element_by_name('lblCc019ScrDispNm').get_attribute("value")
                    administrativedepartment = self.driver.find_element_by_name('lblAc119ScrDispNm').get_attribute("value")
                    classtitle = self.driver.find_element_by_name('lblRepSbjKnjNm').get_attribute("value")
                    dayandperiod = self.driver.find_element_by_name('lstSlbtchinftJ002List_st[0].lblTmtxCd').get_attribute("value")
                    term = self.driver.find_element_by_name('lblAc201ScrDispNm_01').get_attribute("value")
                    date = dayandperiod[0:2]
                    period = dayandperiod[2:5]
                    year = self.driver.find_element_by_name('lblLsnOpcFcy').get_attribute("value")
                    credit = self.driver.find_element_by_name('lblSbjCrnum').get_attribute("value")
                    instructor = self.driver.find_element_by_name('lstChagTch_st[0].lblTchName').get_attribute("value")
                    standardyear = self.driver.find_element_by_name('lblCc004ScrDispNm').get_attribute("value")
                    language = self.driver.find_element_by_name('lblVolCd1').get_attribute("value")
                    special = self.driver.find_element_by_name('lblVolItm1').get_attribute("value")
                    purpose = self.driver.find_element_by_name('lblVolItm2').get_attribute("value")
                    goals = self.driver.find_element_by_name('lblVolItm3').get_attribute("value")
                    format = self.driver.find_element_by_name('lblVolItm43').get_attribute("value")
                    classroom = self.driver.find_element_by_name('lstSlbtchinftJ002List_st[0].lblClrNm').get_attribute("value")

                    print(classcode)
                    print(classtitle)
                    print(campus)
                    print(year)
                    print(administrativedepartment)
                    print(date)
                    print(period)
                    print(term)
                    print(credit)
                    print(instructor)
                    print(standardyear)
                    print(language)
                    print(special)
                    print(purpose)
                    print(goals)
                    print(format)
                    print(classroom)
                    print('')
                    #print(dayandperiod)

                    doc_ref = self.db.collection('selenium')
                    doc_ref.document('serect').collection('scraping').document().set({
                        '授業コード': classcode,
                        'キャンパス': campus,
                        '学部': administrativedepartment,
                        '学期': term,
                        '科目': classtitle,
                        '曜日': date,
                        '時限': period,
                        '開講年度': year,
                        '単位数': credit,
                        '担当者': instructor,
                        '履修基準年度': standardyear,
                        '主な教授言語': language,
                        '特記事項': special,
                        '授業目的': purpose,
                        '到達目標': goals,
                        '授業方法': format,
                        '教室情報': classroom
                    })

                    # ページをスクロールして戻るボタンをクリック
                    sleep(1)
                    self.driver.find_element_by_tag_name('body').click()
                    self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
                    sleep(1)

                    self.driver.find_element_by_xpath('//*[@id="contents"]/div[2]/input').click()
                  
            codenumber1 = self.driver.find_element_by_name('lstSlbinftJ016RList_st[0].lblLsnCd')

            self.driver.find_element_by_name('ENext').click()

            codenumber2 = self.driver.find_element_by_name('lstSlbinftJ016RList_st[0].lblLsnCd')

            if codenumber1 == codenumber2:
              break

                  



                    










        # for i in range(1,16):

        #     #学部
        #     department = self.driver.find_element_by_id('selLsnMngPostCd')
        #     select = Select(department)
        #     department = select.options
        #     select.select_by_value(value)
        #     print(f'{department[i].text}')

        #     #検索ボタンをクリック
        #     self.driver.find_element_by_name('ESearch').click()

        #     # 科目一覧のソースコード取得
        #     page_source = self.driver.page_source
        #     soup = BeautifulSoup(page_source, 'html.parser')

        #     # 詳細見るためのボタンをクリック
        #     class_lists = soup.find_all("tr")[1:]
        #     max_num = len(class_lists)

        #     # 授業格納Object
        #     classinfo = {}
        #     self.driver.find_element_by_name
            
        #     for num in range(2,max_num+1):
        #         sleep(1)
        #         self.driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[2]/table/tbody/tr[{num}]/td[1]/input[1]').click()

        #         classcode = self.driver.find_element_by_name('lblLsnCd').get_attribute("value")
        #         campus = self.driver.find_element_by_name('lblCc019ScrDispNm').get_attribute("value")
        #         administrativedepartment = self.driver.find_element_by_name('lblAc119ScrDispNm').get_attribute("value")
        #         term_offered = self.driver.find_element_by_name('lstSlbtchinftJ002List_st[0].lblAc201ScrDispNm_02').get_attribute("value")
        #         coursenumber = self.driver.find_element_by_name('lblRepSbjKnjNm').get_attribute("value")
        #         dayandperiod = self.driver.find_element_by_name('lstSlbtchinftJ002List_st[0].lblTmtxCd').get_attribute("value")
            
        #         print(i)
        #         print(classcode)
        #         print(campus)
        #         print(administrativedepartment)
        #         print(term_offered)
        #         print(coursenumber)
        #         print(dayandperiod)

        #         doc_ref = self.db.collection('subject')
        #         doc_ref.document('a').collection('b').document().set({
        #             '授業コード': classcode,
        #             '管理部署': administrativedepartment,
        #             '科目': coursenumber,
        #             '曜時': dayandperiod
        #         })

        #         # ページをスクロールして戻るボタンをクリック
        #         sleep(1)
        #         self.driver.find_element_by_tag_name('body').click()
        #         self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        #         sleep(1)

        #         self.driver.find_element_by_xpath('//*[@id="contents"]/div[2]/input').click()

            
        #     #戻るボタンクリック
        #     self.driver.find_element_by_xpath('//*[@id="contents"]/div[2]/input').click()






        # 処理が終わったらwindowを閉じる
        #self.driver.close()
        #self.driver.quit()


        # return json
if __name__ == '__main__':
    driver = Syllabus()
    driver.act('https://syllabus.kwansei.ac.jp/uniasv2/UnSSOLoginControlFree',"21")