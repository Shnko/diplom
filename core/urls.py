from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from core.views import *


class ReportsModel(object):
    """
    Фейковая модель для страниц без данных
    """
    admin_site = admin.site

urlpatterns = [
    path(
        '',
        RedirectView.as_view(url='/reports/summary/'),
    ),
    path(
        'reports/',
        ReportsIndexView.as_view(model_admin=ReportsModel),
        name='reports_index'
    ),
    path(
        'reports/summary/',
        ReportSummaryView.as_view(model_admin=ReportsModel),
        name='report_summary'
    ),
    path(
        'uploads/2145/',
        Upload2145View.as_view(model_admin=ReportsModel),
        name='upload_2145'
    ),
    path(
        'uploads/2146/',
        Upload2146View.as_view(model_admin=ReportsModel),
        name='upload_2146'
    ),
]
