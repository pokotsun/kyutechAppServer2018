# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
from api.management.commands.lib.initialization import initialize_syllabus
from api.models import Syllabus
class Command(BaseCommand):

    # python manage.py helpで表示されるメッセージ
    help = 'シラバスに関するDBの初期化を行う'

    # コマンドライン引数を指定する(argparseモジュール)
    # 今回はblog_idという名前で取得する
    # def add_arguments(self, parser):
    #     parser.add_argument('blog_id', nargs='+', type=int)

    # # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        syllabuses = Syllabus.objects.all()
        syllabuses.delete()
        initialize_syllabus()
