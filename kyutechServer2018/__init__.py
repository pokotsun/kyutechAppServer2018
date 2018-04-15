from django.utils.translation   import ugettext as _, ugettext_lazy
from django.contrib import admin

admin.site.site_title  = ugettext_lazy('管理画面')
admin.site.site_header = ugettext_lazy('九工大アプリ2018サーバー')
admin.site.index_title = ugettext_lazy('九工大アプリ2018')
