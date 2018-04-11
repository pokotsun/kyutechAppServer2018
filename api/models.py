from django.db import models

# Create your models here.

# お知らせの見出しモデル
class NewsHeading(models.Model):
    name = models.CharField(max_length=200) 
    color_code = models.CharField(max_length=20)
    news_heading_code = models.IntegerField(unique=True)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
   
    def __str__(self):
        return self.name 

# Newsモデル
class News(models.Model):
    news_code = models.IntegerField() 
    news_heading_code = models.IntegerField()
    infos = models.CharField(max_length=10000)
    attachement_titles = models.CharField(max_length=10000)
    attachement_urls = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

