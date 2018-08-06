from api.const import NEWS_HEADING_INFOS, SCRAPE_NEWS_URL, YOKE_CODE
from api.models import NewsHeading, News, Syllabus
from api.management.commands.lib.scrape import scrape_news, go_to_next_news
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from api.management.commands.lib.selenium_scrape import init_html_state, get_soup, scrape_syllabus

# NewsHeadingのデータを初期化する
def init_news_heading():
    for info in NEWS_HEADING_INFOS:
        news_heading = NewsHeading(
        short_name=info["short_name"],
        name=info["name"],
        field_names=YOKE_CODE.join(info["fields"]),
        attachment_count = info["attachment_num"],
        news_heading_code=info["news_heading_code"],
        color_code=info["color_code"])

        news_heading.save()

    print("NewsHeadingの初期データの挿入に成功しました！")

# News情報の初期化
def init_news():
    news_init_infos = NEWS_HEADING_INFOS

    for info in news_init_infos:
        news = scrape_news(info["init_url"], info["news_heading_code"])
        if news is not None:
            news.save()
        while news is not None:
            news = go_to_next_news(news)
            if news is not None:
                news.save()
            else:
                print(f"最新のニュースです")
                break

# シラバス情報の初期化
def initialize_syllabus():
    save_syllabus_driver_datas('278') # 情報工学部(学部生)のデータを取得
    save_syllabus_driver_datas('337') # 情報工学部(院生)のデータを取得


# scholor_code: strのデータをスクレイピングしてDBにセーブする
def save_syllabus_driver_datas(scholor_code):
    driver = init_html_state(scholor_code) # 学科コードを選択
    # シラバス一覧の取得
    syllabus_links = driver.find_elements_by_class_name('js-syllabus-show-link')

    print(f"全部で {len(syllabus_links)}個のシラバスがあります")
    for (i, link) in enumerate(syllabus_links):
        link.click() # linkを呼び出す
        sleep(4)
        soup = get_soup(driver)
        print(f"{i}番目のシラバスを取得しています")
        syllabus = scrape_syllabus(soup)
        syllabus.save()
    driver.quit()
