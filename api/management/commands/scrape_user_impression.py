# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
from api.models.user_impression import UserImpression
from datetime import datetime as dt
from api.management.commands.lib.google_spread_sheat import get_impression_spread_sheat
import pytz

class Command(BaseCommand):

    # python manage.py helpで表示されるメッセージ
    help = 'userImpressionに関するDBの初期化を行う\n'\
        + '初期化の時だけ使う'

    # コマンドライン引数を指定する(argparseモジュール)
    # この例ではblog_idという名前で取得する
    # def add_arguments(self, parser):
    #     parser.add_argument('blog_id', nargs='+', type=int)

    # # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        wks = get_impression_spread_sheat()

        list_of_lists = wks.get_all_values()[2:]
        last_impression = UserImpression.objects.order_by('timestamp').last() # last inserted data
        print(f"LAST_INSERTED_IMPRESSION: {last_impression}")
        jp = pytz.timezone('Asia/Tokyo') # set timezone for naive timezone
        for row in list_of_lists:
            impression = UserImpression(
                timestamp = dt.strptime(row[0], "%Y/%m/%d %H:%M:%S"),
                which_os = row[1],
                evaluation = row[2],
                opinion = row[3],
                request_pd = row[4]
            )
            impression_timestamp = jp.localize(impression.timestamp)
            if impression_timestamp > last_impression.timestamp:
                print(impression)
                impression.save()

