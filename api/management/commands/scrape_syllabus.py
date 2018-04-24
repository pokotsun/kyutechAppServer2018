# -- coding: utf-8 --
from django.core.management.base import BaseCommand, CommandError
import urllib.request, urllib.error
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from api.management.commands.lib.selenium_scrape import initialize_html_state, get_soup, scrape_syllabus
import re
import random

class Command(BaseCommand):

    # python manage.py help count_entryで表示されるメッセージ
    help = 'Seleniumのテスト'

    # # コマンドが実行された時に呼ばれるメソッド
    def handle(self, *args, **options):
        driver = initialize_html_state()

        # シラバス一覧の取得
        syllabus_links = driver.find_elements_by_class_name('js-syllabus-show-link')

        print(f"全部で {len(syllabus_links)}個のシラバスがあります")
        for (i, link) in enumerate(syllabus_links):
            link.click() # linkを呼び出す
            sleep(4)
            soup = get_soup(driver)
            print(f"{i}番目のシラバスを取得しています")
            syllabus = scrape_syllabus(soup)
            syllabus.save()
        driver.quit()
