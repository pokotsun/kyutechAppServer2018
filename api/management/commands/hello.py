from django.core.management.base import BaseCommand, CommandError
import urllib.request, urllib.error
from bs4 import BeautifulSoup

class Command(BaseCommand):

    # python manage.py help count_entryで表示されるメッセージ
    help = 'カスタムコマンドのテスト'

    # コマンドライン引数を指定する(argparseモジュール)
    # 今回はblog_idという名前で取得する
    def add_arguments(self, parser):
        parser.add_argument('blog_id', nargs='+', type=int)

    # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        # アクセスするURL
        url = "http://www.nikkei.com/"
        
        # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
        html = urllib.request.urlopen(url)
        
        # htmlをBeautifulSoupで扱う
        soup = BeautifulSoup(html, "html.parser")
        
        # タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
        title_tag = soup.title
        
        # 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
        title = title_tag.string
        
        # タイトル要素を出力
        print(title_tag)
        
        # タイトルを文字列を出力
        print(title)
