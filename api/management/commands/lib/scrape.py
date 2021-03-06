# -*- coding: utf-8 -*-

import requests
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
from time import sleep
from api.const import SCRAPE_NEWS_URL, YOKE_CODE
from api.models import NewsHeading, News

# 次のNewsに移動する
def go_to_next_news(news):
    # htmlをBeautifulSoupで扱う
    news_heading_code = news.news_heading.news_heading_code
    soup = get_soup(f"{SCRAPE_NEWS_URL}{news.url_params}")

    # ページが存在するかチェックする
    if not exists_target_info(soup):
        # データ削除
        News.get_most_recent_filtered_news(news_heading_code).delete()
        # 削除後，再び最新のデータを取得
        news = News.get_most_recent_filtered_news(news_heading_code)
        go_to_next_news(news)
    else:
        # 次に移動するURLを取得する
        next_tag = soup.find_all(text=re.compile("前へ"))[0].parent
        next_url_params = next_tag.get("href")

        # 次のNewsへのLink先が存在する場合
        if next_url_params is not None:
            sleep(0.5)
            return scrape_news(next_url_params,
                news.news_heading.news_heading_code)
        else: # Newsが最新の状態のためここでログを書いておく
            return None
    
# 情報が削除されているかチェック．存在しない場合, DBから最新を削除
def exists_target_info(soup):
    page_title = soup.find("head").find("title").string
    return not page_title == "エラー - サイボウズ(R) デヂエ(R)"

# スクレイピング先のURLからsoupを取得する
def get_soup(url):
    try:
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        html = response.content
        # html = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        print("404Not Found Errorの発生")
        return None
    else:
        return BeautifulSoup(html, "html.parser") # htmlをBeautifulSoupで返す


# 文字列の最後のYOKE_CODEだけ消す
def remove_last_yoke(txt):
   return txt[:len(txt) - len(YOKE_CODE)]

# urlがnews_urlであるNewsの情報を取得する
def scrape_news(news_url_params, news_heading_code):

    news_heading = NewsHeading.objects.get(
        news_heading_code=news_heading_code)

    scrape_url = f"{SCRAPE_NEWS_URL}{news_url_params}"
    print(f"scrape_url: {scrape_url}")

    # htmlをBeautifulSoupで扱う
    soup = get_soup(scrape_url)

    # 実際にデータベースに入れていく情報を取得していく
    field_tags = soup.find_all(id=re.compile(r"fieldname-[0-9]+"))
    info_tags = soup.find_all(class_=re.compile(r"record-value-[0-9]+"))

    # 初期化
    info_text = ""
    attachment_titles = ""
    attachment_urls = ""

    news_column_count = news_heading.field_count()
    field_names = news_heading.decode_field_names()
    field_names.extend(news_heading.get_attachment_field_names())

    print(f"{len(info_tags)}, {news_column_count}")
    #if len(info_tags) == news_column_count:
    print(f"フィールドネーム: {field_names}")
    for (field_name, info_tag) in zip(field_names, info_tags):
        #field_name = f"{field_tag.string}"
        tt = info_tag.tt
        if tt is not None:
            if tt.string is None:
                required_text = ''.join(tt.strings)
                info_text += required_text
                print(f"{field_name} : {required_text}")
            else:
                info_text += tt.string
                print(f"{field_name} : {tt.string}")
        elif info_tag.a is not None:
            a = info_tag.a
            attachment_titles += f"{a.string}{YOKE_CODE}"
            attachment_urls += f"{a.get('href')}{YOKE_CODE}"
            print(f"{field_name} : title: {a.string}\nhref: {a.get('href')}")
        elif info_tag.string is not None:
            info_text += info_tag.string
            print(f"{field_name} : {info_tag.string}")
        else:
            info_text += ""
            print(f"{field_name} : {info_tag.string}")

        info_text += YOKE_CODE

    # 各種テキストの末尾のYOKE_CODEを取り除く
    info_text = remove_last_yoke(info_text)
    attachment_titles = remove_last_yoke(attachment_titles)
    attachment_urls = remove_last_yoke(attachment_urls)

    print(f"""
    info_text: {info_text}

    atache_titles: {attachment_titles}
    
    attache_urls: {attachment_urls}""")

    return News(
    news_heading = news_heading,
    infos=info_text,
    attachment_titles=attachment_titles,
    attachment_urls=attachment_urls,
    url_params=news_url_params)
