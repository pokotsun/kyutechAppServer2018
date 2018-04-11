"""定数を書いていく"""
# スクレイピングで BASEとなるURL
SCRAPE_BASE_URL = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/" 

# 文を区切るときに使う文字
YOKE_CODE = "|%&%|"

# 初期化時に使う定数群
# NewsHeadingの初期化用
NEWS_HEADING_INFOS = [ 
    {"short_name": "知", "name":"おしらせ(学生向け)", "news_heading_code": 357, "color_code": "#219653"},
    {"short_name": "変", "name":"時間割・講義室変更", "news_heading_code": 391, "color_code": "##6495ED"},
    {"short_name": "休", "name":"休講通知", "news_heading_code": 361, "color_code": "#5F9EA0"},
    {"short_name": "補", "name":"補講通知", "news_heading_code": 363, "color_code": "#EF924E"},
    {"short_name": "呼", "name":"学生呼出", "news_heading_code": 393, "color_code": "#EB5757"},
    {"short_name": "試", "name":"授業調整・期末試験", "news_heading_code": 364, "color_code": "#FA8072"},
    {"short_name": "手", "name":"各種手続き", "news_heading_code": 373, "color_code": "#4682B4"},
    {"short_name": "奨", "name":"奨学金", "news_heading_code": 367, "color_code": "#FFD700"},
    {"short_name": "集", "name":"集中講義", "news_heading_code": 379, "color_code": "#87CEEB"},
    {"short_name": "留", "name":"留学・国際関連", "news_heading_code": 372, "color_code": "#D2691E"},
    {"short_name": "学", "name":"学部生情報", "news_heading_code": 368, "color_code": "#AA1F19"},
    {"short_name": "院", "name":"大学院生情報", "news_heading_code": 370, "color_code": "#FF69B4"},
]
