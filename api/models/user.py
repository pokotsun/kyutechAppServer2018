from django.db import models

# ユーザーモデル
class User(models.Model):
    SCHOOL_FIRST = 1
    SCHOOL_SECOND = 2
    SCHOOL_THIRD = 3
    SCHOOL_FOURTH = 4

    DEPARTMENT_JOHO_TINO = 21
    DEPARTMENT_JOHO_TSUSHIN = 22
    DEPARTMENT_JOHO_SYSTEM = 23
    DEPARTMENT_JOHO_BUTSURI = 24
    DEPARTMENT_JOHO_SEIMEI = 25

    SCHOOL_SET = (
        (SCHOOL_FIRST, "1回生"),
        (SCHOOL_SECOND, "2回生"),
        (SCHOOL_THIRD, "3回生"),
        (SCHOOL_FOURTH, "4回生"),
    )

    DEPARTMENT_SET = (
        (DEPARTMENT_JOHO_TINO, "情報工学部　知能情報工学科"),
        (DEPARTMENT_JOHO_TSUSHIN, "情報工学部　情報・通信工学科"),
        (DEPARTMENT_JOHO_SYSTEM, "情報工学部　知的システム工学科"),
        (DEPARTMENT_JOHO_BUTSURI, "情報工学部　物理情報工学科"),
        (DEPARTMENT_JOHO_SEIMEI, "情報工学部　生命情報工学科"),
    )

    class Meta:
        verbose_name_plural = 'Users'

    school_year = models.IntegerField(default=SCHOOL_FIRST, choices=SCHOOL_SET)
    department = models.IntegerField(default=DEPARTMENT_JOHO_TINO, choices=DEPARTMENT_SET)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"user_id: {self.pk}, {self.school_year}年, {self.department}"
