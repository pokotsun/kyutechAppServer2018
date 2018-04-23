# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
import urllib.request, urllib.error
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import re

class Command(BaseCommand):

    # python manage.py help count_entryで表示されるメッセージ
    help = 'Seleniumのテスト'

    # # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1280,1024')

        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://edragon-syllabus.jimu.kyutech.ac.jp/guest/syllabuses') # ページを開く
        print(driver.title) #=> 九州工業大学シラバス
        faculty_select = driver.find_element_by_id('belong_children_faculty') # エレメントを取得する
        faculty_select_element = Select(faculty_select)
        faculty_select_element.select_by_value('278')
    
        driver.find_element_by_class_name('js-simple-search-btn').click() # 検索ボタンをクリック


        sleep(5)
        syllubuse_links = driver.find_elements_by_class_name('js-syllabus-show-link')

        #print(syllubuse_links)
        for (i, link) in enumerate(syllubuse_links):
            if i < 5:
                link.click()
                sleep(5)
                # ここまで来たらデータをsoupから取得できる
                data = driver.page_source.encode('utf-8')
                soup = BeautifulSoup(data, "html.parser")
                
                # シラバスの情報を取っていく
                subject_name = soup.find(class_="syllabus__subject-name")
                print(f"教科名: {subject_name.string}")

                subject_content = subject_name.parent.next_sibling
                while subject_content is not None:
                    print(f"{subject_content.string}")
                    subject_content = subject_content.next_sibling                
                print("\n")

                # コンテンツ情報を取得していく
                section_titles = soup.find_all(class_=re.compile(r"syllabus__section__title"))
                for section_title in section_titles:
                    section_content = section_title.next_sibling
                    #print(f"{section_title.string}: {syllabus_section_content.get_text()}")

                    if section_content.string is not None:
                        print(f"{section_title.string}: {section_content.string}")
                    else: #中に入れ子でタグを持っている場合
                        print(f"{section_title.string}: {section_content.get_text()}")

                print("\n******************************\n")
                    

                #print(soup.title)
                #driver.save_screenshot(f"test{i}.png")
            else:
                break

        driver.quit()
