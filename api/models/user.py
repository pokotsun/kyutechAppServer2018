from django.db import models

# ユーザーモデル
class User(models.Model):
    class Meta:
        verbose_name_plural = 'Users'

    school_year = models.IntegerField(default=1)
    department = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{school_year}, {department}, {created_at}"
