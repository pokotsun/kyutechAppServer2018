from django.contrib import admin

from .models.news import News
from .models.news_heading import  NewsHeading
from .models.syllabus import Syllabus
from .models import User, UserSchedule, SchoolYear, Department
# Register your models here.

class NewsInline(admin.TabularInline):
    model = News
    extra = 3

# Newsの表示
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'news_heading', 'attachment_titles', 'attachment_urls', 'created_at', 'updated_at')
    list_filter = ['news_heading', 'created_at']
    search_fields = ['infos']

# NewsHeadingの表示
class NewsHeadingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'short_name', 'news_heading_code', 'color_code', 'updated_at')

    fieldsets = [
        (None, {'fields': ['name', 'news_heading_code', 'color_code', 'field_names']}),
    ]
    inlines = [NewsInline]

# Syllabusの表示
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'teacher_name', 'target_period')
    list_filter = ['target_period']
    search_fields = ['title']

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', "school_year", "department")
    # list_filter = ['school_year_id', 'department_id']


class UserScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'syllabus', 'day', 'period', 'quarter', 'is_valid')
    list_filter = ['day']


# NewsHeadingの表示
class SchoolYearAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'unique_code')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'unique_code')

admin.site.register(NewsHeading, NewsHeadingAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Syllabus, SyllabusAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserSchedule, UserScheduleAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(Department, DepartmentAdmin)