from django.contrib import admin
from django.urls import path

from core.views import *


class ReportsModel(object):
    """
    Фейковая модель для страниц без данных
    """
    admin_site = admin.site

urlpatterns = [
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
        'reports/1000/',
        Report1000View.as_view(model_admin=ReportsModel),
        name='report_1000'
    ),
    path(
        'reports/2100/',
        Report2100View.as_view(model_admin=ReportsModel),
        name='report_2100'
    ),
    path(
        'reports/2120/',
        Report2120View.as_view(model_admin=ReportsModel),
        name='report_2120'
    ),
    path(
        'reports/2140/',
        Report2140View.as_view(model_admin=ReportsModel),
        name='report_2140'
    ),
    path(
        'reports/2145/',
        Report2145View.as_view(model_admin=ReportsModel),
        name='report_2145'
    ),
    path(
        'reports/2146/',
        Report2146View.as_view(model_admin=ReportsModel),
        name='report_2146'
    ),
    path(
        'reports/2150/',
        Report2150View.as_view(model_admin=ReportsModel),
        name='report_2150'
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
