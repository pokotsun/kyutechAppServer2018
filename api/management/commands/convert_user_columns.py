# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
from api.management.commands.lib.initialization import init_departments
from api.models import User, SchoolYear, Department

class Command(BaseCommand):

    # python manage.py helpで表示されるメッセージ
    help = "Userのスキーマを変えるための一時的な変更のためのスクリプト"

    # コマンドライン引数を指定する(argparseモジュール)
    # 今回はblog_idという名前で取得する
    # def add_arguments(self, parser):
    #     parser.add_argument('blog_id', nargs='+', type=int)

    # # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        # caution!!!!
        users = User.objects.all()
        for u in users:
            year_code = u.school_year_id
            department_code = u.department_id
            year = SchoolYear.objects.get(unique_code=year_code)
            department = Department.objects.get(unique_code=department_code)
            u.school_yearZ = year
            u.departmentZ = department
            u.save()

        print("success convert users!")
 