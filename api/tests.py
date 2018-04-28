from django.test import TestCase

import datetime
from .models import News, Syllabus, User, UserSchedule
from django.urls import reverse

# Create your tests here.
class UserScheduleModelTests(TestCase):
    def test_新しいユーザーで時間割を作る(self):
    #def test_newusertest(self):
        user = User.objects.create(school_year=1, department=11)
        syllabus = Syllabus.objects.create()

        schedule = UserSchedule.objects.create(
            user = 0,
            syllabus = 0,
            day = 3,
            period = 3,
            quarter = 2,
            is_valid = True,
        )
        print(f"item_numbers = {UserSchedule.objects.all()}")
        self.assertEqual(len(UserSchedule.objects.all()), 2)


def create_dummy_syllabus():
    return Syllabus.objects.create(
        title="", subject_code=1,
        teacher_name="", target_participants="",
    )
