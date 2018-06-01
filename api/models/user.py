from django.db import models
import api.const as const

# ユーザーモデル
class User(models.Model):
    SCHOOL_FIRST = 0
    SCHOOL_SECOND = 1
    SCHOOL_THIRD = 2
    SCHOOL_FOURTH = 3

    DEPARTMENT_JOKO11 = 200
    DEPARTMENT_JOKO12 = 201
    DEPARTMENT_JOKO23 = 202
    DEPARTMENT_JOKO34 = 203
    DEPARTMENT_JOKO35 = 204
    DEPARTMENT_JOHO_TINO = 205
    DEPARTMENT_JOHO_TINO_HENNYU = 206
    DEPARTMENT_JOHO_TSUSHIN = 207
    DEPARTMENT_JOHO_TSUSHIN_HENNYU = 208
    DEPARTMENT_JOHO_SYSTEM = 209
    DEPARTMENT_JOHO_SYSTEM_HENNYU = 210
    DEPARTMENT_JOHO_BUTSURI = 211
    DEPARTMENT_JOHO_BUTSURI_HENNYU = 212
    DEPARTMENT_JOHO_SEIMEI = 213
    DEPARTMENT_JOHO_SEIMEI_HENNYU = 214

    SCHOOL_SET = (
        (SCHOOL_FIRST, "1回生"),
        (SCHOOL_SECOND, "2回生"),
        (SCHOOL_THIRD, "3回生"),
        (SCHOOL_FOURTH, "4回生"),
    )

    DEPARTMENT_SET = (
        (DEPARTMENT_JOKO11, "情報工学部　情工１類　Ⅰクラス"),
        (DEPARTMENT_JOKO12, "情報工学部　情工１類　Ⅱクラス"),
        (DEPARTMENT_JOKO23, "情報工学部　情工２類　Ⅲクラス"),
        (DEPARTMENT_JOKO34, "情報工学部　情工３類　Ⅳクラス"),
        (DEPARTMENT_JOKO35, "情報工学部　情工３類　Ⅴクラス"),
        (DEPARTMENT_JOHO_TINO, "情報工学部　知能情報工学科"),
        (DEPARTMENT_JOHO_TINO_HENNYU, "情報工学部　知能情報工学科　知能情報工学科（編入）"),
        (DEPARTMENT_JOHO_TSUSHIN, "情報工学部　電子情報工学科"),
        (DEPARTMENT_JOHO_TSUSHIN_HENNYU, "情報工学部　電子情報工学科　電子情報工学科（編入）"),
        (DEPARTMENT_JOHO_SYSTEM, "情報工学部　システム創成情報工学科　システム創成情報工学科"),
        (DEPARTMENT_JOHO_SYSTEM_HENNYU, "情報工学部　システム創成情報工学科　システム創成情報工学科（編入）"),
        (DEPARTMENT_JOHO_BUTSURI, "情報工学部　機械情報工学科　機械情報工学科"),
        (DEPARTMENT_JOHO_BUTSURI_HENNYU, "情報工学部　機械情報工学科　機械情報工学科（編入）"),
        (DEPARTMENT_JOHO_SEIMEI, "情報工学部　生命情報工学科　生命情報工学科"),
        (DEPARTMENT_JOHO_SEIMEI_HENNYU, "情報工学部　生命情報工学科　生命情報工学科（編入）"),
    )

    class Meta:
        verbose_name_plural = 'Users'

    school_year = models.IntegerField(default=SCHOOL_FIRST, choices=SCHOOL_SET)
    department = models.IntegerField(default=DEPARTMENT_JOHO_TINO, choices=DEPARTMENT_SET)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 各学科に割り当てられたidから学科名を取得する
    def department_name(self):
        try:
            return next(v for k,v in User.DEPARTMENT_SET if k == self.department)
        except StopIteration:
            return "情報工学部　情工１類　Ⅰクラス"

    def __str__(self):
        return f"user_id: {self.pk}, {self.school_year}年, {self.department}"
