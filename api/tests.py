from django.test import TestCase

import datetime
from .models import News, Syllabus, User, UserSchedule, NewsHeading
from .management.commands.lib.scrape import get_soup, scrape_news
from django.urls import reverse

# Create your tests here.
# class UserScheduleModelTests(TestCase):
#     def test_新しいユーザーで時間割を作る(self):
#     #def test_newusertest(self):
#         user = User.objects.create(school_year=1, department=11)
#         syllabus = Syllabus.objects.create()
#
#         schedule = UserSchedule.objects.create(
#             user = 0,
#             syllabus = 0,
#             day = 3,
#             period = 3,
#             quarter = 2,
#             is_valid = True,
#         )
#         print(f"item_numbers = {UserSchedule.objects.all()}")
#         self.assertEqual(len(UserSchedule.objects.all()), 2)

# ダミーのシラバスを作る
def create_dummy_syllabus():
    return Syllabus.objects.create(
        title="", subject_code=1,
        teacher_name="", target_participants="",
    )

class NewsScrapeTests(TestCase):
    def test_学生呼出のスクレイピングで空の添付資料が起きる(self):
            news_heading = NewsHeading(
            short_name="呼",
            name="学生呼出",
            field_names="件名|%&%|注記|%&%|対象学科等|%&%|対象学年|%&%|内容|%&%|特記|%&%|日付|%&%|終了",
            attachement_count = 5,
            news_heading_code=393,
            color_code="#FFFFFF")
            news_heading.save()

            news = scrape_news(
            "db.cgi?page=DBRecord&did=393&qid=all&vid=24&rid=123&head=22&hid=206&sid=n&fvid=132#dz_navigation>",
            393
            )
            self.assertEqual(news.attachement_titles, "")
