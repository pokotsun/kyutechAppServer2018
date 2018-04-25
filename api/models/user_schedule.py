from django.db import models
from api.models.syllabus import Syllabus
from api.models.user import User

# ユーザーモデル
class UserSchedule(models.Model):
    class Meta:
        verbose_name_plural = 'UserSchedules'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    day = models.IntegerField()
    period = models.IntegerField()
    quarter = models.IntegerField()
    is_valid = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""{self.user}, {self.syllabus},
        {Syllabus.convert_day(self.day), {Syllabus.convert_period(self.period)}}"""
