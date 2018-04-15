# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
import urllib.request, urllib.error
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#from api.management.commands import aiueo
#import os

class Command(BaseCommand):

    # python manage.py help count_entryで表示されるメッセージ
    help = 'カスタムコマンドのテスト'



    # コマンドライン引数を指定する(argparseモジュール)
    # 今回はblog_idという名前で取得する
    # def add_arguments(self, parser):
    #     parser.add_argument('blog_id', nargs='+', type=int)
    #
    # # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1280,1024')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.google.co.jp/')
        print(driver.title) #=> Google
        driver.save_screenshot('test.png')
