# -*- coding: utf-8 -*-

import urllib.request, urllib.error
from bs4 import BeautifulSoup
import api.const as const
import re
from time import sleep

# 次のNewsに移動する
def go_to_next_news(current_news_url, news_column_count, news_heading_code):
    # htmlをBeautifulSoupで扱う
    soup = get_soup(current_news_url)

    # 次に移動するURLを取得する
    next_tag = soup.find_all(text=re.compile("前へ"))[0].parent
    next_url = next_tag.get("href")
    print(f"next_url: {next_url}\n")
    
    # 次のNewsへのLink先が存在しなかった場合
    if next_url is not None:
        sleep(0.5)
        scrape_news(next_url, news_column_count, news_heading_code)            
    else: # Newsが最新の状態のためここでログを書いておく
        print(f"最新のニュースです")

# スクレイピング先のURLからsoupを取得する
def get_soup(news_url):
    # アクセスするURL
    url = f"{const.SCRAPE_BASE_URL}{news_url}"
    
    try: 
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        print("404Not Found Errorの発生")
        return None
    else: 
        # htmlをBeautifulSoupで返す
        return BeautifulSoup(html, "html.parser")

# urlがnews_urlであるNewsの情報を取得する
def scrape_news(news_url, news_column_count, news_heading_code):
    news_heading_code = re.search("[0-9]+", re.search("did=[0-9]+", news_url).group()).group()
    print(news_heading_code)

    # htmlをBeautifulSoupで扱う
    soup = get_soup(news_url)

    # 前のと次のニュースのリンク先を取得する
    next_tag = soup.find_all(text=re.compile("前へ"))[0].parent
    next_url = next_tag.get("href")
    before_tag = soup.find_all(text=re.compile("次へ"))[0].parent
    before_url = before_tag.get("href")

    # 実際にデータベースに入れていく情報を取得していく
    title_tags = soup.find_all(id=re.compile(r"fieldname-[0-9]+"))
    info_tags = soup.find_all(class_=re.compile(r"record-value-[0-9]+"))

    print(f"next_url: {next_url}\n")
    print(f"before_url: {before_url}\n")
    
    info_text = ""
    yoke_code = const.YOKE_CODE
    
    for (i, info_tag) in enumerate(info_tags):
        tt = info_tag.tt
        if tt != None:
            if tt.string == None:
                required_text = ''.join(tt.strings)
                info_text += required_text 
                print(f"{i}: {required_text}")
            else: 
                info_text += tt.string 
                print(f"{i}: {tt.string}")
        elif info_tag.a != None:
            a = info_tag.a
            info_text += a.string + yoke_code + a.get('href') 
            print(f"{i}: title: {a.string}\nhref: {a.get('href')}")
        elif info_tag.string != None: 
            info_text += info_tag.string 
            print(f"{i}: {info_tag.string}")
        else: 
            info_text += ""
            print(f"{i}: {info_tag.string}")

        info_text += yoke_code 

    print(f"info_text: {info_text.encode().decode('utf-8')}")
    
    go_to_next_news(news_url, news_column_count, news_heading_code)

