# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Command(BaseCommand):

    # python manage.py helpで表示されるメッセージ
    help = 'departmentに関するDBの初期化を行う'

    # コマンドライン引数を指定する(argparseモジュール)
    # 今回はblog_idという名前で取得する
    # def add_arguments(self, parser):
    #     parser.add_argument('blog_id', nargs='+', type=int)

    # # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']

        credentials = ServiceAccountCredentials.from_json_keyfile_name('kyutechApp2018-ce3ddcfd4eba.json', scope)
        gc = gspread.authorize(credentials)
        # worksheat情報の取得
        wks = gc.open('九工大アプリ2018アンケートフォーム（回答）').sheet1

        list_of_lists = wks.get_all_values()[2:]
        for row in list_of_lists:
            print(row)

# wks.update_acell('A1', 'Hello World!')
# print(wks.acell('A1'))