# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
from api.management.commands.lib.initialization import init_news, init_news_heading
from api.models import NewsHeading

class Command(BaseCommand):

    # python manage.py help で表示されるメッセージ
    help = '学生お知らせに関するDBの初期化を行う'

    # コマンドライン引数を指定する(argparseモジュール)
    # 今回はblog_idという名前で取得する
    # def add_arguments(self, parser):
    #     parser.add_argument('blog_id', nargs='+', type=int)

    # # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        NewsHeading.objects.all().delete() # すでにあるNewsHeadingを全削除 同時に紐付いているNewsも全削除される
        init_news_heading()
        init_news()
