from api.const import NEWS_HEADING_INFOS, SCRAPE_BASE_URL, YOKE_CODE
from api.models import NewsHeading, News
from api.management.commands.lib.scrape import scrape_news, go_to_next_news
def initialize_news_heading():
    for info in NEWS_HEADING_INFOS:
        news_heading = NewsHeading(
        short_name=info["short_name"],
        name=info["name"], 
        field_names=YOKE_CODE.join(info["fields"]),
        attachement_count = info["attachement_num"],
        news_heading_code=info["news_heading_code"], 
        color_code=info["color_code"])

        news_heading.save()
        
    print("NewsHeadingの初期データの挿入に成功しました！")

# News情報の初期化
def initialize_news():
    news_init_infos = NEWS_HEADING_INFOS

    for info in news_init_infos:
        news = scrape_news(info["init_url"], info["news_heading_code"])
        if news is not None: 
            news.save()
        while news is not None:
        #for i in range(3):
            news = go_to_next_news(news)
            if news is not None:
                news.save()
            else: 
                print(f"最新のニュースです")
                break
