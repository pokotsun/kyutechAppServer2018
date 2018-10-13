"""定数を書いていく"""
# スクレイピングで BASEとなるURL
SCRAPE_NEWS_URL = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/"
SCRAPE_SYLLABUS_URL = "https://edragon-syllabus.jimu.kyutech.ac.jp/guest/syllabuses"

# 文を区切るときに使う文字列
YOKE_CODE = "|%&%|"

# 初期化時に使う定数群
# NewsHeadingの初期化用
NEWS_HEADING_INFOS = [
    {
        "short_name": "知",
        "name":"おしらせ(学生向け)",
        "news_heading_code": 357,
        "color_code": "#219653",
        "fields": ["タイトル", "日付", "時限等", "場所", "内容", "対象学科", "対象学年"],
        "attachment_num": 5,
        "init_url": "db.cgi?page=DBRecord&did=357&qid=all&vid=24&rid=7&sid=n&fvid=136#dz_navigation",
    },
    {
        "short_name": "変",
        "name":"時間割・講義室変更",
        "news_heading_code": 391,
        "color_code": "#6495ED",
        "fields": ["タイトル", "科目名", "教員名", "対象学科", "対象学年", "日付", "時限", "種別", "変更前", "変更後", "内容"],
        "attachment_num": 0,
        "init_url": "db.cgi?page=DBRecord&did=391&qid=all&vid=24&rid=4&Head=24&hid=265&sid=n&rev=0&ssid=3-2042-7255-g72"
    },
    {
        "short_name": "休",
        "name":"休講通知",
        "news_heading_code": 361,
        "color_code": "#5F9EA0",
        "fields": ["日付", "時限", "休講科目", "担当教員", "教室", "対象学科", "対象学年", "特記"],
        "attachment_num": 0,
        "init_url": "db.cgi?page=DBRecord&did=361&qid=all&vid=24&rid=3&sid=n&fvid=128#dz_navigation"
    },
    {   "short_name": "補",
        "name":"補講通知",
        "news_heading_code": 363,
        "color_code": "#EF924E",
        "fields": ["日付", "時限", "補講科目", "担当教員", "教室", "対象学科", "対象学年", "特記"],
        "attachment_num": 0,
        "init_url": "db.cgi?page=DBRecord&did=363&qid=all&vid=24&rid=2&Head=21&hid=201&sid=n&rev=0&ssid=1-2808-5151-g72"
    },
    {
        "short_name": "呼",
        "name":"学生呼出",
        "news_heading_code": 393,
        "color_code": "#EB5757",
        "fields": ["件名", "注記", "対象学科等", "対象学年", "内容", "特記", "日付", "終了"],
        "attachment_num": 5,
        "init_url": "db.cgi?page=DBRecord&did=393&qid=all&vid=24&rid=2&Head=22&hid=206&sid=n&rev=0&ssid=1-2833-5161-g72"
    },
    {
        "short_name": "試",
        "name":"授業調整・期末試験",
        "news_heading_code": 364,
        "color_code": "#FA8072",
        "fields": ["タイトル", "日付", "時限等", "場所", "内容", "対象学科", "対象学年", "担当教員"],
        "attachment_num": 5,
        "init_url": "db.cgi?page=DBRecord&did=364&qid=all&vid=24&rid=1&Head=24&hid=231&sid=n&rev=0&ssid=1-2861-5172-g72"
    },
    {
        "short_name": "手",
        "name":"各種手続き",
        "news_heading_code": 373,
        "color_code": "#4682B4",
        "fields": ["件名", "担当部署", "内容", "注記", "日付"],
        "attachment_num": 4,
        "init_url": "db.cgi?page=DBRecord&did=373&qid=all&vid=24&rid=1&Head=&hid=&sid=n&rev=0&ssid=1-2963-5213-g72"
    },
    {
        "short_name": "奨",
        "name":"奨学金",
        "news_heading_code": 367,
        "color_code": "#FFD700",
        "fields": ["件名", "種別", "期日", "内容"],
        "attachment_num": 2,
        "init_url": "db.cgi?page=DBRecord&did=367&qid=all&vid=24&rid=4&Head=28&hid=199&sid=n&rev=0&ssid=1-2991-5222-g72"
    },
    {
        "short_name": "集",
        "name":"集中講義",
        "news_heading_code": 379,
        "color_code": "#87CEEB",
        "fields": ["タイトル", "日付", "内容", "備考"],
        "attachment_num": 5,
        "init_url": "db.cgi?page=DBRecord&did=379&qid=all&vid=24&rid=3&Head=25&hid=202&sid=n&rev=0&ssid=1-3019-5237-g72"
    },
    {
        "short_name": "留",
        "name":"留学・国際関連",
        "news_heading_code": 372,
        "color_code": "#D2691E",
        "fields": ["タイトル", "担当部署", "内容", "日付"],
        "attachment_num": 4,
        "init_url": "db.cgi?page=DBRecord&did=372&qid=all&vid=24&rid=3&Head=22&hid=196&sid=n&rev=0&ssid=1-3043-5246-g72"
    },
    {
        "short_name": "学",
        "name":"学部生情報",
        "news_heading_code": 368,
        "color_code": "#AA1F19",
        "fields": ["件名", "内容", "備考"],
        "attachment_num": 5,
        "init_url": "db.cgi?page=DBRecord&did=368&qid=all&vid=24&rid=5&Head=&hid=&sid=n&rev=0&ssid=1-3074-5271-g72"
    },
    {
        "short_name": "院",
        "name":"大学院生情報",
        "news_heading_code": 370,
        "color_code": "#FF69B4",
        "news_heading_code": 370,
        "fields": ["件名", "内容", "備考"],
        "attachment_num": 5,
        "init_url": "db.cgi?page=DBRecord&did=370&qid=all&vid=24&rid=2&Head=&hid=&sid=n&rev=0&ssid=1-3093-5278-g72"
    },
]

# school_yearの静的な値
SCHOOL_NAME_SET = (
    ("学部1年", "学部1年"),
    ("学部2年", "学部2年"),
    ("学部3年", "学部3年"),
    ("学部4年", "学部4年"),
    ("修士1年", "修士1年"),
    ("修士2年", "修士2年"),
)


SCHOOL_CODE_SET = (
    (0, "学部1年"),
    (1, "学部2年"),
    (2, "学部3年"),
    (3, "学部4年"),
    (4, "修士1年"),
    (5, "修士2年"),
)


#departmentのnameの静的な値
DEPARTMENT_NAME_SET = (
    ("情報工学部　情工１類　Ⅰクラス", "情報工学部　情工１類　Ⅰクラス"),
    ("情報工学部　情工１類　Ⅱクラス", "情報工学部　情工１類　Ⅱクラス"),
    ("情報工学部　情工２類　Ⅲクラス", "情報工学部　情工２類　Ⅲクラス"),
    ("情報工学部　情工３類　Ⅳクラス", "情報工学部　情工３類　Ⅳクラス"),
    ("情報工学部　情工３類　Ⅴクラス", "情報工学部　情工３類　Ⅴクラス"),
    ("情報工学部　知能情報工学科", "情報工学部　知能情報工学科"),
    ("情報工学部　知能情報工学科　知能情報工学科（編入）", "情報工学部　知能情報工学科　知能情報工学科（編入）"),
    ("情報工学部　電子情報工学科", "情報工学部　電子情報工学科"),
    ("情報工学部　電子情報工学科　電子情報工学科（編入）", "情報工学部　電子情報工学科　電子情報工学科（編入）"),
    ("情報工学部　システム創成情報工学科　システム創成情報工学科", "情報工学部　システム創成情報工学科　システム創成情報工学科"),
    ("情報工学部　システム創成情報工学科　システム創成情報工学科（編入）", "情報工学部　システム創成情報工学科　システム創成情報工学科（編入）"),
    ("情報工学部　機械情報工学科　機械情報工学科", "情報工学部　機械情報工学科　機械情報工学科"),
    ("情報工学部　機械情報工学科　機械情報工学科（編入）", "情報工学部　機械情報工学科　機械情報工学科（編入）"),
    ("情報工学部　生命情報工学科　生命情報工学科", "情報工学部　生命情報工学科　生命情報工学科"),
    ("情報工学部　生命情報工学科　生命情報工学科（編入）", "情報工学部　生命情報工学科　生命情報工学科（編入）"),
    ("大学院情報工学府博士前期課程　情報創成工学専攻　情報創成工学専門分野", "大学院情報工学府博士前期課程　情報創成工学専攻　情報創成工学専門分野"),
    ("大学院情報工学府博士前期課程　先端情報工学専攻　知能情報工学専門分野", "大学院情報工学府博士前期課程　先端情報工学専攻　知能情報工学専門分野"),
    ("大学院情報工学府博士前期課程　先端情報工学専攻　電子情報工学専門分野", "大学院情報工学府博士前期課程　先端情報工学専攻　電子情報工学専門分野"),
    ("大学院情報工学府博士前期課程　学際情報工学専攻　システム創成情報工学専門分野", "大学院情報工学府博士前期課程　学際情報工学専攻　システム創成情報工学専門分野"),
    ("大学院情報工学府博士前期課程　学際情報工学専攻　生命情報工学専門分野", "大学院情報工学府博士前期課程　学際情報工学専攻　生命情報工学専門分野"),
    ("大学院情報工学府博士前期課程　学際情報工学専攻　機械情報工学専門分野", "大学院情報工学府博士前期課程　学際情報工学専攻　機械情報工学専門分野"),
)



# departmentのunique_codeの静的な値
DEPARTMENT_JOKO11 = 200
DEPARTMENT_JOKO12 = 201
DEPARTMENT_JOKO23 = 202
DEPARTMENT_JOKO34 = 203
DEPARTMENT_JOKO35 = 204
DEPARTMENT_JOHO_CHINO = 205
DEPARTMENT_JOHO_CHINO_HENNYU = 206
DEPARTMENT_JOHO_DENSHI = 207
DEPARTMENT_JOHO_DENSHI_HENNYU = 208
DEPARTMENT_JOHO_SYSTEM = 209
DEPARTMENT_JOHO_SYSTEM_HENNYU = 210
DEPARTMENT_JOHO_KIKAI = 211
DEPARTMENT_JOHO_KIKAI_HENNYU = 212
DEPARTMENT_JOHO_SEIMEI = 213
DEPARTMENT_JOHO_SEIMEI_HENNYU = 214
DEPARTMENT_JOHO_M_JOHOSOSEI_JOHOSOSEI = 215
DEPARTMENT_JOHO_M_SENTAN_CHINO = 216
DEPARTMENT_JOHO_M_SENTAN_DENSHI = 217
DEPARTMENT_JOHO_M_GAKUSAI_SYSTEM = 218
DEPARTMENT_JOHO_M_GAKUSAI_SEIMEI = 219
DEPARTMENT_JOHO_M_GAKUSAI_KIKAI = 220


DEPARTMENT_CODE_SET = (
    (DEPARTMENT_JOKO11, "情報工学部　情工１類　Ⅰクラス"),
    (DEPARTMENT_JOKO12, "情報工学部　情工１類　Ⅱクラス"),
    (DEPARTMENT_JOKO23, "情報工学部　情工２類　Ⅲクラス"),
    (DEPARTMENT_JOKO34, "情報工学部　情工３類　Ⅳクラス"),
    (DEPARTMENT_JOKO35, "情報工学部　情工３類　Ⅴクラス"),
    (DEPARTMENT_JOHO_CHINO, "情報工学部　知能情報工学科"),
    (DEPARTMENT_JOHO_CHINO_HENNYU, "情報工学部　知能情報工学科　知能情報工学科（編入）"),
    (DEPARTMENT_JOHO_DENSHI, "情報工学部　電子情報工学科"),
    (DEPARTMENT_JOHO_DENSHI_HENNYU, "情報工学部　電子情報工学科　電子情報工学科（編入）"),
    (DEPARTMENT_JOHO_SYSTEM, "情報工学部　システム創成情報工学科　システム創成情報工学科"),
    (DEPARTMENT_JOHO_SYSTEM_HENNYU, "情報工学部　システム創成情報工学科　システム創成情報工学科（編入）"),
    (DEPARTMENT_JOHO_KIKAI, "情報工学部　機械情報工学科　機械情報工学科"),
    (DEPARTMENT_JOHO_KIKAI_HENNYU, "情報工学部　機械情報工学科　機械情報工学科（編入）"),
    (DEPARTMENT_JOHO_SEIMEI, "情報工学部　生命情報工学科　生命情報工学科"),
    (DEPARTMENT_JOHO_SEIMEI_HENNYU, "情報工学部　生命情報工学科　生命情報工学科（編入）"),
    (DEPARTMENT_JOHO_M_JOHOSOSEI_JOHOSOSEI, "大学院情報工学府博士前期課程　情報創成工学専攻　情報創成工学専門分野"),
    (DEPARTMENT_JOHO_M_SENTAN_CHINO, "大学院情報工学府博士前期課程　先端情報工学専攻　知能情報工学専門分野"),
    (DEPARTMENT_JOHO_M_SENTAN_DENSHI, "大学院情報工学府博士前期課程　先端情報工学専攻　電子情報工学専門分野"),
    (DEPARTMENT_JOHO_M_GAKUSAI_SYSTEM, "大学院情報工学府博士前期課程　学際情報工学専攻　システム創成情報工学専門分野"),
    (DEPARTMENT_JOHO_M_GAKUSAI_SEIMEI, "大学院情報工学府博士前期課程　学際情報工学専攻　生命情報工学専門分野"),
    (DEPARTMENT_JOHO_M_GAKUSAI_KIKAI, "大学院情報工学府博士前期課程　学際情報工学専攻　機械情報工学専門分野"),
)

