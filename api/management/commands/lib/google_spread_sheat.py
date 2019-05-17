import gspread
from oauth2client.service_account import ServiceAccountCredentials
from const import USER_IMPRESSION_WORK_SHEAT_NAME, SPREAD_SHEAT_CERT_JSON

# get user impression work sheat
def get_impression_spread_sheat():
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SPREAD_SHEAT_CERT_JSON, scope)
    gc = gspread.authorize(credentials)
    return gc.open(USER_IMPRESSION_WORK_SHEAT_NAME).sheet1