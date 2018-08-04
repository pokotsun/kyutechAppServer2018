# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
import urllib.request, urllib.error
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from api.management.commands.lib.selenium_scrape import init_html_state, get_soup, scrape_syllabus
import re
import random

class Command(BaseCommand):

    # python manage.py helpで表示されるメッセージ
    help = 'スクレイピングのテスト'

    # # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):

        with open('prettify.html', 'r') as f:
            html = f.read()  # ファイル終端まで全て読んだデータを返す

            soup = BeautifulSoup(html, "html.parser")
            subject_title = soup.find(class_="syllabus__subject-name")
            print(f"教科名: {subject_title.string}")

            subject_content_tables = subject_title.parent.parent.find_all("table")

            if len(subject_content_tables) == 2:
                table = subject_content_tables[0]
                tr_list = table.find_all("tr")

                for tr in tr_list:
                    th_list = tr.find_all("th")
                    td_list = tr.find_all("td")
                    for (th, td) in zip(th_list, td_list):
                        print(f"thead: {th.string}\n td: {td.string}\n")

                table = subject_content_tables[1]
                tr_list = table.find_all("tr")
                for (i, tr) in enumerate(tr_list):
                    print(f"{tr.get_text()}")

            f.close()
