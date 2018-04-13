# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
from api.management.commands.lib.scrape import scrape_news
import sys

class Command(BaseCommand):

    # python manage.py help count_entryで表示されるメッセージ
    help = 'Newsの情報を取ってくる'

    # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        sys.setrecursionlimit(10000)

        scrape_news("db.cgi?page=DBRecord&did=357&qid=all&vid=24&rid=7&sid=n&fvid=136#dz_navigation", 12, 357)

