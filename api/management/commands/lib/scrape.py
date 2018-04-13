# -*- coding: utf-8 -*-

import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
from time import sleep
from api.const import SCRAPE_BASE_URL, YOKE_CODE, NEWS_HEADING_INFOS
from api.models import NewsHeading, News

# 次のNewsに移動する
def go_to_next_news(news, news_column_count):
    # htmlをBeautifulSoupで扱う
    soup = get_soup(f"{SCRAPE_BASE_URL}{news.url_params}")

    # 次に移動するURLを取得する
    next_tag = soup.find_all(text=re.compile("前へ"))[0].parent
    next_url_params = next_tag.get("href")
    
    # 次のNewsへのLink先が存在しなかった場合
    if next_url_params is not None:
        sleep(0.5)
        return scrape_news(next_url_params,
            news_column_count, news.news_heading.news_heading_code)            
    else: # Newsが最新の状態のためここでログを書いておく
        print(f"最新のニュースです")
        return None

# スクレイピング先のURLからsoupを取得する
def get_soup(url):
    # アクセスするURL
    try: 
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        print("404Not Found Errorの発生")
        return None
    else: 
        # htmlをBeautifulSoupで返す
        return BeautifulSoup(html, "html.parser")

# 文字列の最後のYOKE_CODEだけ消す
def remove_last_yoke(txt):
   return txt[:len(txt) - len(YOKE_CODE)] 

# urlがnews_urlであるNewsの情報を取得する
def scrape_news(news_url_params, news_column_count, news_heading_code):
    #news_heading_code = re.search("[0-9]+", 
    #re.search("did=[0-9]+", news_url_params).group()).group()
    
    news_heading = NewsHeading.objects.get(
        news_heading_code=news_heading_code) 

    scrape_url = f"{SCRAPE_BASE_URL}{news_url_params}"
    # htmlをBeautifulSoupで扱う
    soup = get_soup(scrape_url)

    # 実際にデータベースに入れていく情報を取得していく
    field_tags = soup.find_all(id=re.compile(r"fieldname-[0-9]+"))
    info_tags = soup.find_all(class_=re.compile(r"record-value-[0-9]+"))
    
    # 初期化
    info_text = attachement_titles = attachement_urls = ""
    
    field_names = [x["fields"] for x in NEWS_HEADING_INFOS if x["news_heading_code"] == news_heading.news_heading_code][0]
    print(field_names)

    print(f"{len(info_tags)}, {news_column_count}")
    if len(info_tags) == news_column_count:
        for (field_tag, info_tag) in zip(field_tags, info_tags):
            field_name = f"{field_tag.string}"
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
                #info_text += a.string + YOKE_CODE + a.get('href') 
                attachement_titles += f"{a.string}{YOKE_CODE}"
                attachement_urls += f"{a.get('href')}{YOKE_CODE}"
                print(f"{field_name} : title: {a.string}\nhref: {a.get('href')}")
            elif info_tag.string is not None: 
                info_text += info_tag.string 
                print(f"{field_name} : {info_tag.string}")
            else: 
                info_text += ""
                print(f"{field_name} : {info_tag.string}")

            info_text += YOKE_CODE 

        info_text = remove_last_yoke(info_text)
        attachement_titles = remove_last_yoke(attachement_titles)
        attachement_urls = remove_last_yoke(attachement_urls)

        return News(
        news_heading = news_heading,
        infos=info_text,
        attachement_titles=attachement_titles,
        attachement_urls=attachement_urls,
        url_params=news_url_params)
    else:
        print("情報の数とフィールドの数が合いません")
