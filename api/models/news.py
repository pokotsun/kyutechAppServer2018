from django.db import models
from ..const import YOKE_CODE, SCRAPE_NEWS_URL
from api.models.news_heading import NewsHeading
import re

# Create your models here.

# Newsモデル
class News(models.Model):
    class Meta:
        verbose_name_plural = 'News'

    news_heading = models.ForeignKey(NewsHeading, on_delete=models.CASCADE)
    infos = models.CharField(max_length=10000)
    attachment_titles = models.CharField(max_length=10000, null=True)
    attachment_urls = models.CharField(max_length=10000, null=True)
    url_params = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"news_heading: {self.news_heading}\nurl_params: {self.url_params}"

    # あるNewsHeadingに属するものだけ取得
    def filter_by_news_heading_code(news_heading_code):
        return News.objects.filter(news_heading__news_heading_code__contains=news_heading_code)

    def get_most_recent_filtered_news(news_heading_code):
        return News.filter_by_news_heading_code(news_heading_code).reverse().first()

    # 各種モデル上の情報をデコードする関数 filterをかけることで空文字を返り値のリストから削除
    def decode_infos(self):
        return filter(lambda x: bool(x), self.infos.split(YOKE_CODE))

    def decode_attachment_titles(self):
        return filter(lambda x: bool(x), self.attachment_titles.split(YOKE_CODE))

    def decode_attachment_urls(self):
        return map(lambda x: x if re.match("http(s)?://.*", x) and not(re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-z0-9]+(?:\.[a-zA-Z0-9-]+)*$", x)) else f"{SCRAPE_NEWS_URL}{x}", 
            filter(lambda x: bool(x), self.attachment_urls.split(YOKE_CODE))
        )

    # saveのオーバーライド
    # Newsがsaveされた場合そのNewsの親となるNewsHeadingのupdated_atを更新させたいため
    def save(self):
        super().save()
        self.news_heading.save()
