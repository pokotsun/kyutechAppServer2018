# -*- coding: utf-8 -*-

import urllib.request, urllib.error
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import re
from api.models import Syllabus

# htmlの状態をシラバスが取れる状態までする
def initialize_html_state():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,1024')

    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://edragon-syllabus.jimu.kyutech.ac.jp/guest/syllabuses') # ページを開く
    print(driver.title) #=> 九州工業大学シラバス
    faculty_select = driver.find_element_by_id('belong_children_faculty') # selectboxエレメントをidから取得
    faculty_select_element = Select(faculty_select) # セレクトボックスを取得
    faculty_select_element.select_by_value('278') # 情報工学部を選択

    driver.find_element_by_class_name('js-simple-search-btn').click() # 検索ボタンをクリック
    sleep(5) # 検索ボタン結果が反映されるまで待つ

    return driver

# seleniumドライバーからsoupを取得する
def get_soup(driver):
    data = driver.page_source.encode('utf-8')
    return BeautifulSoup(data, "html.parser")

# テーブルの値を取得していく
def _get_table_contents(table_tag):
    tbody = table_tag.tbody
    if tbody is not None:
        tr_list = tbody.find_all('tr')
        result = ""
        for tr in tr_list:
            result += f"{tr.get_text()}\n"
        return result.rstrip("\n")
    else: #空の時は空文字を返す
        return ""

# シラバスの情報を取っていく
def scrape_syllabus(soup):

    syllabus = Syllabus() # モデルの初期化
    subject_title = soup.find(class_="syllabus__subject-name")
    syllabus.set_title(subject_title.string)
    print(f"教科名: {subject_title.string}")

    subject_content = subject_title.parent.next_sibling
    while subject_content is not None:
        attr_infos = subject_content.string.split('】')
        label = attr_infos[0].lstrip('【')
        value = ','.join(filter(lambda str: str != '', re.split(r'[, ]', attr_infos[1])))
        print(f"{label}: {value}\n")
        syllabus.set_model_attribute(label, value) # 属性のセット

        subject_content = subject_content.next_sibling # 次のエレメントをセット

    # コンテンツ情報を取得していく
    section_titles = soup.find_all(class_=re.compile(r"syllabus__section__title"))
    for section_title in section_titles:
        section_content = section_title.next_sibling
        if section_content.string is not None:
            print(f"{section_title.string}: {section_content.string}\n")
            syllabus.set_model_attribute(section_title.string, section_content.string) # 属性のセット
        else: #中に入れ子でタグを持っている場合
            if section_title.string in "授業項目":
                value = _get_table_contents(section_content)
                syllabus.set_model_attribute(section_title.string, value)
                print(f"{section_title.string}: \n{value}\n")
            else:
                print(f"{section_title.string}: {section_content.get_text()}\n")
                syllabus.set_model_attribute(section_title.string, section_content.get_text()) # 属性のセット

    print("\n*****************************************************************\n")
    return syllabus
    #driver.save_screenshot(f"test{i}.png")
