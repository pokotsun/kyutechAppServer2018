from django.db import models
import api.const as const

class Department(models.Model):
    class Meta:
        verbose_name_plural = "Departments"

    name = models.CharField(max_length=50, default=const.DEPARTMENT_NAME_SET[0][0], choices=const.DEPARTMENT_NAME_SET)
    unique_code = models.IntegerField(default=const.DEPARTMENT_JOKO11, choices=const.DEPARTMENT_CODE_SET, db_index=True)


    def __str__(self):
        return f"department_id: {self.pk}, name: {self.name}, unique_code: {self.unique_code}"