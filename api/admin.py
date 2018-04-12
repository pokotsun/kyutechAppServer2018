from django.contrib import admin

from .models import NewsHeading, News
# Register your models here.

class NewsInline(admin.TabularInline):
    model = News
    extra = 3

# Newsの表示
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_heading', 'created_at', 'updated_at')

# NewsHeadingの表示
class NewsHeadingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'short_name', 'news_heading_code', 'color_code')

    fieldsets = [ 
        (None, {'fields': ['name', 'news_heading_code', 'color_code']}),
    ]   
    inlines = [NewsInline]    

    
admin.site.register(NewsHeading, NewsHeadingAdmin)
admin.site.register(News, NewsAdmin)

