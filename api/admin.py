from django.contrib import admin

from .models.news import News
from .models.news_heading import  NewsHeading
from .models.syllabus import Syllabus
# Register your models here.

class NewsInline(admin.TabularInline):
    model = News
    extra = 3

# Newsの表示
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_heading', 'attachement_titles', 'attachement_urls', 'created_at', 'updated_at')
    list_filter = ['news_heading', 'created_at']

# NewsHeadingの表示
class NewsHeadingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'short_name', 'news_heading_code', 'color_code', 'updated_at')

    fieldsets = [
        (None, {'fields': ['name', 'news_heading_code', 'color_code']}),
    ]
    inlines = [NewsInline]

# Syllabusの表示
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher_name', 'target_hour', 'academic_credit')

admin.site.register(NewsHeading, NewsHeadingAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Syllabus, SyllabusAdmin)
