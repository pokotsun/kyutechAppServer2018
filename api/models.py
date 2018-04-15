from django.db import models
from .const import YOKE_CODE

# Create your models here.

# お知らせの見出しモデル
class NewsHeading(models.Model):
    class Meta:
        verbose_name_plural = 'NewsHeadings' 

    name = models.CharField(max_length=200) 
    short_name = models.CharField(max_length=2)
    color_code = models.CharField(max_length=20)
    news_heading_code = models.IntegerField(unique=True)
    field_names = models.CharField(max_length=1000)
    attachement_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name 

    # フィールド数を返す
    def field_count(self):
        return len(self.field_names.split(YOKE_CODE)) + self.attachement_count

    def decode_field_names(self):
         return self.field_names.split(YOKE_CODE)

    def get_attachement_field_names(self):
        return [f"添付資料({x+1})" for x in range(self.attachement_count)]

# Newsモデル
class News(models.Model):
    class Meta:
        verbose_name_plural = 'News'

    news_heading = models.ForeignKey(NewsHeading, on_delete=models.CASCADE)
    infos = models.CharField(max_length=10000)
    attachement_titles = models.CharField(max_length=10000, null=True)
    attachement_urls = models.CharField(max_length=10000, null=True)
    url_params = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def decode_infos(self):
        return self.infos.split(YOKE_CODE)

    def decode_attachement_titles(self):
        return self.attachement_titles.split(YOKE_CODE)

    def decode_attachement_urls(self):
        return self.attachement_urls.split(YOKE_CODE)
    
