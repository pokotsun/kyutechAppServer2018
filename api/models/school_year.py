from django.db import models
import api.const as const

class SchoolYear(models.Model):
    class Meta:
        verbose_name_plural = "SchoolYears"

    name = models.CharField(max_length=300, default=const.SCHOOL_NAME_SET[0][0], choices=const.SCHOOL_NAME_SET)
    id = models.IntegerField(default=0, choices=const.SCHOOL_CODE_SET, db_index=True, primary_key=True)


    def __str__(self):
        return f"schoolyear_id: {self.id}, name: {self.name}"