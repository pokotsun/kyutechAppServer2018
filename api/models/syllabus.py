from django.db import models
from datetime import datetime


class Syllabus(models.Model):
    class Meta:
        verbose_name_plural = 'Syllabus'

    title = models.CharField(max_length=100)
    subject_code = models.IntegerField(unique=True)
    teacher_name = models.CharField(max_length=50)
    target_participants = models.CharField(max_length=300, null=True)
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
    notes = models.CharField(max_length=500, null=True)
    professor_email = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Syllabus: {self.title}\nteacher_name: {self.teacher_name}"


    # 各属性をセットする なんとか綺麗にしたい
    def set_model_attribute(self, label, value):
        if label in "【科目コード】":
            self.subject_code = int(value)
        elif label in "【担当教員】":
            self.teacher_name = value
        elif label in "【学部・学科】":
            self.target_participants = value
        elif label in "【単位区分】":
            self.academic_credit = value
        elif label in "【単位数】":
            self.academic_credit_num = int(value)
        elif label in "【対象学年】":
            self.target_class = value
        elif label in "【開講学期】":
            self.target_term = value
        elif label in "【クラス】":
            self.class_number = int(value)
        elif label in "【曜日・時限】":
            self.target_hour = value
        elif label in "【講義室】":
            self.target_place = value
        elif label in "【更新日】":
            date_info = value.split(",")[0].split("/")
            self.published_date = datetime(
                date_info[0], date_info[1], date_info[2]
            )
        elif label in "授業の概要":
            self.abstract = value
        elif label in "カリキュラムにおけるこの授業の位置付け":
            self.positioning = value
        elif label in "授業項目":
            self.lecture_content = value
        elif label in "授業の進め方":
            self.lecture_processing = value
        elif label in "授業の達成目標（学習・教育到達目標との関連）":
            self.performance_target = value
        elif label in "成績評価の基準および評価方法:":
            self.valuation_basis = value
        elif label in "授業外学習（予習・復習）の指示":
            self.instruction_out_learning = value
        elif label in "キーワード":
            self.keyword = value
        elif label in "教科書":
            self.text_book = value
        elif label in "参考書":
            self.study_aid_books = value
        elif label in "備考":
            self.notes = value
        elif label in "電子メールアドレス":
            self.professor_email = value
        else:
            print(f"{label}は指定のラベルではありません。\n value: {value}")
