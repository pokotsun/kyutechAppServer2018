# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
import urllib.request, urllib.error
from api.const import NEWS_HEADING_INFOS 
from api.management.commands.lib.initialization import initialize_news, initialize_news_heading

#from api.management.commands import aiueo

class Command(BaseCommand):

    # python manage.py help count_entryで表示されるメッセージ
    help = 'DBの初期化を行う'

    # コマンドライン引数を指定する(argparseモジュール)
    # 今回はblog_idという名前で取得する
    # def add_arguments(self, parser):
    #     parser.add_argument('blog_id', nargs='+', type=int)
    
    # # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        #initialize_news()
        initialize_news_heading()
