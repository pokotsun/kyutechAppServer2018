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
from api.const import SCRAPE_SYLLABUS_URL

# htmlの状態をシラバスが取れる状態までする ドライバーを返す
def init_html_state(scholor_code):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,1024')

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(f"{SCRAPE_SYLLABUS_URL}") # ページを開く
    print(driver.title) #=> 九州工業大学シラバス

    syllabus_year_select = driver.find_element_by_id('q_lecture_year_eq') # selectBoxエレメントをidから取得
    syllabus_year_select = Select(syllabus_year_select) # セレクトボックスを取得
    syllabus_year_select.select_by_value("2019") # 年度を選択

    faculty_select = driver.find_element_by_id('belong_children_faculty') # selectboxエレメントをidから取得
    faculty_select_element = Select(faculty_select) # セレクトボックスを取得
    faculty_select_element.select_by_value(scholor_code) # 学部を選択

    driver.find_element_by_class_name('js-simple-search-btn').click() # 検索ボタンをクリック
    sleep(10) # 検索ボタン結果が反映されるまで待つ

    return driver

# seleniumドライバーからsoupを取得する
def get_soup(driver):
    data = driver.page_source.encode('utf-8')
    return BeautifulSoup(data, "html.parser")

# テーブルの値を取得する
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
    syllabus = Syllabus(open_year=2019) # モデルの初期化, 開講年度の作成
    subject_title = soup.find(class_="syllabus__subject-name")
    syllabus.set_title(subject_title.string)
    print(f"教科名: {subject_title.string}")

    # while subject_content is not None:
    #     attr_infos = subject_content.string.split('】')
    #     label = attr_infos[0].lstrip('【')
    #     value = ','.join(filter(lambda str: str != '', re.split(r'[, ]', attr_infos[1])))
    #     print(f"{label}: {value}\n")
    #     syllabus.set_model_attribute(label, value) # 属性のセット
    #
    #     subject_content = subject_content.next_sibling # 次のエレメントをセット

    subject_content_tables = subject_title.parent.parent.find_all("table")

    if len(subject_content_tables) == 2:
        table = subject_content_tables[0]
        tr_list = table.find_all("tr")

        for tr in tr_list:
            th_list = tr.find_all("th")
            td_list = tr.find_all("td")
            for (th, td) in zip(th_list, td_list):
                label = th.string or ""
                value = td.string or ""
                syllabus.set_model_attribute(label, value)
                print(f"{th.string}: {td.string}\n")

        # 学部情報
        table = subject_content_tables[1]
        tr_list = table.find_all("tr")
        value = ""
        for (i, tr) in enumerate(tr_list):
            # content_list = tr.children
            if i != 0:
                value += ','.join(tr.strings) + "\n"
        value.lstrip("\n")
        print(f"{value}")
        syllabus.academic_credit_infos = value

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
