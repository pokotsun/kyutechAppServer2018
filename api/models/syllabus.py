from django.db import models
from datetime import datetime


class Syllabus(models.Model):
    class Meta:
        verbose_name_plural = 'Syllabus'

    title = models.CharField(max_length=100)
    subject_code = models.IntegerField(unique=True)
    teacher_name = models.CharField(max_length=50)
    attended_students = models.CharField(max_length=300, null=True)
    academic_credit = models.CharField(max_length=100, null=True)
    academic_credit_num = models.IntegerField()
    target_class = models.CharField(max_length=100)
    target_term = models.CharField(max_length=100)
    class_number = models.IntegerField()
    target_hour = models.CharField(max_length=200)
    target_place = models.CharField(max_length=150)
    published_date = models.DateTimeField()

    abstract = models.CharField(max_length=1000)
    positioning = models.CharField(max_length=1000)
    lecture_content = models.CharField(max_length=1000)
    lecture_processing = models.CharField(max_length=1000)
    performance_target = models.CharField(max_length=1000)
    valuation_basis = models.CharField(max_length=1000)
    instruction_out_learning = models.CharField(max_length=1000, null=True)
    keyword = models.CharField(max_length=500, null=True)
    text_book = models.CharField(max_length=500, null=True)
    study_aid_books = models.CharField(max_length=500, null=True)
    professor_email = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Syllabus: {self.title}\nteacher_name: {self.teacher_name}"


    # セクション属性をセットする
    def set_model_section_attribute(self, label, value):
        if label == "【科目コード】":
            self.subject_code = int(value)
        elif label == "【担当教員】":
            self.teacher_name = value
        elif label == "【学部・学科】":
            self.attended_students = value
        elif label == "【単位区分】":
            self.academic_credit = value
        elif label == "【単位数】":
            self.academic_credit_num = int(value)
        elif label == "【対象学年】":
            self.target_class = value
        elif label == "【開講学期】":
            self.target_term = value
        elif label == "【クラス】":
            self.class_number = int(value)
        elif label == "【曜日・時限】":
            self.target_hour = value
        elif label == "【講義室】":
            self.target_place = value
        elif label == "【更新日】":
            date_info = value.split(",")[0].split("/")
            self.published_date = datetime(
                date_info[0], date_info[1], date_info[2]
            )
        else:
            print(f"{label}は指定のラベルではありません。\n value: {value}")
