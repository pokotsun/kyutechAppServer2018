from django.db import models
import api.const as const

class Department(models.Model):
    class Meta:
        verbose_name_plural = "Departments"

    name = models.CharField(max_length=50, default=const.DEPARTMENT_NAME_SET[0][0], choices=const.DEPARTMENT_NAME_SET)
    id = models.IntegerField(choices=const.DEPARTMENT_CODE_SET, db_index=True, primary_key=True)


    def __str__(self):
        return f"department_id: {self.id}, name: {self.name}"