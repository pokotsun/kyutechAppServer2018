from django.db import models
from api.models.syllabus import Syllabus
from api.models.user import User

# ユーザーモデル
class UserSchedule(models.Model):
    MON_DAY = FIRST_PERIOD = FIRST_QUARTER =  0
    TUES_DAY = SECOND_PERIOD = SECOND_QUARTER = 1
    WEDNES_DAY = THIRD_PERIOD = THIRD_QUARTER = 2
    THURS_DAY = FOURTH_PERIOD = FOURTH_QUARTER = 3
    FRI_DAY = FIFTH_PERIOD = 4

    DAY_SET = (
        (MON_DAY, "月曜"),
        (TUES_DAY, "火曜"),
        (WEDNES_DAY, "水曜"),
        (THURS_DAY, "木曜"),
        (FRI_DAY, "金曜"),
    )

    PERIOD_SET = (
        (FIRST_PERIOD, "1限"),
        (SECOND_PERIOD, "2限"),
        (THIRD_PERIOD, "3限"),
        (FOURTH_PERIOD, "4限"),
        (FIFTH_PERIOD, "5限"),
    )

    QUARTER_SET = (
        (FIRST_QUARTER, "第1クオーター"),
        (SECOND_QUARTER, "第2クオーター"),
        (THIRD_QUARTER, "第3クオーター"),
        (FOURTH_QUARTER, "第4クオーター"),
    )

    class Meta:
        verbose_name_plural = 'UserSchedules'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    day = models.IntegerField(default=MON_DAY, choices=DAY_SET)
    period = models.IntegerField(default=FIFTH_PERIOD, choices=PERIOD_SET)
    quarter = models.IntegerField(default=FIRST_QUARTER, choices=QUARTER_SET)
    is_valid = models.BooleanField(default=True)
    memo = models.CharField(max_length=300, default="")
    late_num = models.IntegerField(default=0)
    absent_num = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.user}, {self.syllabus}, is_valid: {self.is_valid}"
