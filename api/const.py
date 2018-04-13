"""定数を書いていく"""
# スクレイピングで BASEとなるURL
SCRAPE_BASE_URL = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/" 

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
        "attachement_num": 5,
        "init_url": "db.cgi?page=dbrecord&did=357&qid=all&vid=24&rid=7&head=33&hid=247&sid=n&rev=0&ssid=1-794-15679-g90"
    },
    {
        "short_name": "変", 
        "name":"時間割・講義室変更", 
        "news_heading_code": 391, 
        "color_code": "##6495ED",
        "fields": ["タイトル", "科目名", "教員名", "対象学科", "対象学年", "日付", "時限", "種別", "変更前", "変更後", "内容"],
        "attachement_num": 0,
        "init_url": "db.cgi?page=dbrecord&did=391&qid=all&vid=24&rid=4&head=24&hid=265&sid=n&rev=0&ssid=1-845-15710-g90"
    },
    {
        "short_name": "休", 
        "name":"休講通知", 
        "news_heading_code": 361, 
        "color_code": "#5F9EA0",
        "fields": ["日付", "時限", "休講科目", "担当教員", "教室", "対象学科", "対象学年", "特記"],
        "attachement_num": 0,
        "init_url": "db.cgi?page=DBRecord&did=361&qid=all&vid=24&rid=3&sid=n&fvid=128#dz_navigation"
    },
    {   "short_name": "補", 
        "name":"補講通知", 
        "news_heading_code": 363, 
        "color_code": "#EF924E",
        "fields": ["日付", "時限", "補講科目", "担当教員", "教室", "対象学科", "対象学年", "特記"],
        "attachement_num": 0,
        "init_url": "db.cgi?page=DBRecord&did=363&qid=all&vid=24&rid=2&Head=21&hid=201&sid=n&rev=0&ssid=1-2808-5151-g72"
    },
    {
        "short_name": "呼", 
        "name":"学生呼出", 
        "news_heading_code": 393, 
        "color_code": "#EB5757",
        "fields": ["件名", "注記", "対象学科等", "対象学年", "内容", "特記", "日付", "終了"],
        "attachement_num": 5,
        "init_url": "db.cgi?page=DBRecord&did=393&qid=all&vid=24&rid=2&Head=22&hid=206&sid=n&rev=0&ssid=1-2833-5161-g72"
    },
    {
        "short_name": "試", 
        "name":"授業調整・期末試験", 
        "news_heading_code": 364, 
        "color_code": "#FA8072",
        "fields": ["タイトル", "日付", "時限等", "場所", "内容", "対象学科", "対象学年", "担当教員"],
        "attachement_num": 5,
        "init_url": "db.cgi?page=DBRecord&did=364&qid=all&vid=24&rid=1&Head=24&hid=231&sid=n&rev=0&ssid=1-2861-5172-g72"
    },
    {
        "short_name": "手", 
        "name":"各種手続き", 
        "news_heading_code": 373, 
        "color_code": "#4682B4",
        "fields": ["件名", "担当部署", "内容", "注記", "日付"],
        "attachement_num": 4,
        "init_url": "db.cgi?page=DBRecord&did=373&qid=all&vid=24&rid=1&Head=&hid=&sid=n&rev=0&ssid=1-2963-5213-g72"
    },
    {
        "short_name": "奨", 
        "name":"奨学金", 
        "news_heading_code": 367, 
        "color_code": "#FFD700",
        "fields": ["件名", "種別", "期日", "内容"],
        "attachement_num": 2,
        "init_url": "db.cgi?page=DBRecord&did=367&qid=all&vid=24&rid=4&Head=28&hid=199&sid=n&rev=0&ssid=1-2991-5222-g72"
    },
    {
        "short_name": "集", 
        "name":"集中講義", 
        "news_heading_code": 379, 
        "color_code": "#87CEEB",
        "fields": ["タイトル", "日付", "内容", "備考"],
        "attachement_num": 5,
        "init_url": "db.cgi?page=DBRecord&did=379&qid=all&vid=24&rid=3&Head=25&hid=202&sid=n&rev=0&ssid=1-3019-5237-g72"
    },
    {
        "short_name": "留", 
        "name":"留学・国際関連", 
        "news_heading_code": 372, 
        "color_code": "#D2691E",
        "fields": ["タイトル", "担当部署", "内容", "日付"],
        "attachement_num": 4,
        "init_url": "db.cgi?page=DBRecord&did=372&qid=all&vid=24&rid=3&Head=22&hid=196&sid=n&rev=0&ssid=1-3043-5246-g72"
    },
    {
        "short_name": "学", 
        "name":"学部生情報", 
        "news_heading_code": 368, 
        "color_code": "#AA1F19",
        "fields": ["件名", "内容", "備考"],
        "attachement_num": 5,
        "init_url": "db.cgi?page=DBRecord&did=368&qid=all&vid=24&rid=5&Head=&hid=&sid=n&rev=0&ssid=1-3074-5271-g72"
    },
    {
        "short_name": "院", 
        "name":"大学院生情報", 
        "news_heading_code": 370, 
        "color_code": "#FF69B4",
        "news_heading_code": 370, 
        "fields": ["件名", "内容", "備考"],
        "attachement_num": 5,
        "init_url": "db.cgi?page=DBRecord&did=370&qid=all&vid=24&rid=2&Head=&hid=&sid=n&rev=0&ssid=1-3093-5278-g72"
    },
]
