from django.db import models
import api.const as const

# ユーザーの感想
class UserImpression(models.Model):

    class Meta:
        verbose_name_plural = 'UserImpression'

    timestamp = models.DateTimeField()
    which_os = models.CharField(max_length=10)
    evaluation = models.CharField(max_length=500)
    opinion = models.CharField(max_length=512)
    p_and_d_opinion = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f""
