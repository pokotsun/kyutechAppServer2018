from django.db import models
from datetime import datetime
import re


class Syllabus(models.Model):
    class Meta:
        verbose_name_plural = 'Syllabus'

    _day_list = (
        ("m.*", "月曜"),
        ("tu.*", "火曜"),
        ("w.*", "水曜"),
        ("th.*", "木曜"),
        ("f.*", "金曜"),
        (".*", "月曜"),
    )

    title = models.CharField(max_length=255)
    subject_code = models.IntegerField()
    teacher_name = models.CharField(max_length=100)
    academic_credit_infos = models.CharField(max_length=1024)
    target_school_year = models.CharField(max_length=255)
    target_term = models.CharField(max_length=255)
    class_number = models.IntegerField()
    target_period = models.CharField(max_length=255)
    target_place = models.CharField(max_length=255)
    published_date = models.DateTimeField()

    abstract = models.CharField(max_length=2550)
    positioning = models.CharField(max_length=2550)
    lecture_content = models.CharField(max_length=2550)
    lecture_processing = models.CharField(max_length=2550)
    performance_target = models.CharField(max_length=2550)
    valuation_basis = models.CharField(max_length=2550)
    instruction_out_learning = models.CharField(max_length=2550, null=True)
    keywords = models.CharField(max_length=1024, null=True)
    text_books = models.CharField(max_length=1024, null=True)
    study_aid_books = models.CharField(max_length=2048, null=True)
    notes = models.CharField(max_length=1024, null=True)
    professor_email = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}: {self.title}  {self.teacher_name}"

    # タイトルをsetする
    def set_title(self, title):
        self.title = title

    # TODO ここのコードなんとか綺麗にしたい
    # 各属性をセットする
    def set_model_attribute(self, label, value):
        label = re.sub(r'[【】]', "", label)

        if label in "【科目コード】":
            self.subject_code = int(value)
        elif label in "【担当教員】":
            self.teacher_name = value
        elif label in "【対象学年】":
            self.target_school_year = value
        elif label in "【開講学期】":
            self.target_term = value
        elif label in "【クラス】":
            self.class_number = int(value)
        elif label in "【曜日・時限】":
            self.target_period = value.replace(" ", "")
        elif label in "【講義室】":
            self.target_place = value
        elif label in "【更新日】":
            date_info = [int(x) for x in value.split()[0].split("/")]
            self.published_date = datetime(date_info[0], date_info[1], date_info[2])
        elif label in "授業の概要":
            self.abstract = value
        elif label in "カリキュラムにおけるこの授業の位置付け" or label in "カリキュラムにおけるこの授業の位置づけ":
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
            self.keywords = value
        elif label in "教科書":
            self.text_books = value
        elif label in "参考書":
            self.study_aid_books = value
        elif label in "備考":
            self.notes = value
        elif label in "電子メールアドレス":
            self.professor_email = value
        else:
            print(f"{label}は指定のラベルではありません。\n value: {value}")
            raise ValueError

    # dayとperiodでフィルターしたSyllabusリストを返す day: "mon" ~ "fri", period: "0" ~ "4"
    def filter_by_day_and_period(day_code, period_code):
        day = Syllabus.convert_day(day_code)
        period = Syllabus.convert_period(period_code)
        if day is not None and period is not None:
            return Syllabus.objects.filter(
                target_period__contains=f"{day}{period}"
            )
        else:
            return None

    # 学科名でfilter
    def filter_by_department(department_name):
        if department_name is not None:
            return Syllabus.objects.filter(academic_credit_infos__contains=department_name)
        else:
            return None

    # dayコードをDB検索用の文字列に変換
    def convert_day(day_code):
        return next(v for k,v in Syllabus._day_list if re.match(k, day_code))

    def convert_period(period_code):
        if re.match("[0-4]", period_code):
            return str(int(period_code) + 1) + "限"
        else:
            return None
