from django.db import models
from api.models.school_year import SchoolYear
from api.models.department import Department
import api.const as const

# ユーザーモデル
class User(models.Model):

    class Meta:
        verbose_name_plural = 'Users'

    school_year = models.ForeignKey(SchoolYear, null=True, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, null=True, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 各学科に割り当てられたidから学科名を取得する
    def department_name(self):  
        return self.department.name

    def __str__(self):
        return f"user_id: {self.pk}, {self.school_year_id}年, {self.department_id}"
