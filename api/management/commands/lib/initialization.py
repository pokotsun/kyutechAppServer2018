from api.const import NEWS_HEADING_INFOS
from api.models import NewsHeading

def initialize_news_heading():
    for info in NEWS_HEADING_INFOS:
        news_heading = NewsHeading(
        short_name=info["short_name"],
        name=info["name"], 
        news_heading_code=info["news_heading_code"], 
        color_code=info["color_code"])

        news_heading.save()
        
    print("Newsの初期データの追加に成功しました！")
