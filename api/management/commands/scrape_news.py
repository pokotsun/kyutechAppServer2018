# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
from api.management.commands.lib.scrape import scrape_news
from api.models import NewsHeading, News
from api.management.commands.lib.scrape import go_to_next_news

class Command(BaseCommand):

    # python manage.py help scrape_newsで表示されるメッセージ
    help = 'Newsの情報を取ってくる'

    # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        news_headings = NewsHeading.objects.all()

        # NewsHeadingそれぞれに対して属しているNewsを取得していく
        for news_heading in news_headings:
            news = News.get_most_recent_filtered_news(news_heading.news_heading_code)
            while news is not None:
                news = go_to_next_news(news)
                if news is not None:
                    news.save()
                else:
                    print(f"{news_heading.name}は最新の状態に更新されました!")
                    break
