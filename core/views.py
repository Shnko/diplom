import sys
from inspect import isclass

from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, TemplateView
from unfold.views import UnfoldModelAdminViewMixin

from core.forms import DateRangeInputForm
from core.models import Child
from core.reports import build_report_2120, build_report_summary


# Create your views here.
class ReportsIndexView(UnfoldModelAdminViewMixin, TemplateView):
    """
    Страница со списком отчётов
    """
    template_name = "reports/reports_index.html"
    title = "Отчёты"
    permission_required = ()

    def __init__(self, model_admin, **kwargs):
        super().__init__(model_admin, **kwargs)
        reports = []
        for item in vars(sys.modules[__name__]).items():
            if isclass(item[1]) and issubclass(item[1], FormView) and issubclass(item[1], UnfoldModelAdminViewMixin):
                reports += [{"title": item[1].title, "url": item[1].reverse_name}]
        self.extra_context = {
            "reports": reports,
        }

class ReportSummaryView(UnfoldModelAdminViewMixin, FormView):
    template_name = "reports/reports_base.html"
    title = "Отчёт по форме №41"
    form_class = DateRangeInputForm
    permission_required = ()
    reverse_name = "report_summary"

    def get_success_url(self):
        return reverse(self.reverse_name)

    def post(self, request, *args, **kwargs):
        form = DateRangeInputForm(request.POST)
        if form.is_valid():
            report_file_name = build_report_summary(form.cleaned_data['start'], form.cleaned_data['end'])
            return FileResponse(open(report_file_name, 'rb'), as_attachment=True, filename=f'{self.title}.xlsx')
        else:
            return HttpResponseRedirect('#')


class Report1000View(UnfoldModelAdminViewMixin, FormView):
    template_name = "reports/reports_base.html"
    title = "Отчёт 1000 - Дома ребёнка"
    form_class = DateRangeInputForm
    permission_required = ()
    reverse_name = 'report_1000'

    def get_success_url(self):
        return reverse(self.reverse_name)

class Report2100View(UnfoldModelAdminViewMixin, FormView):
    template_name = "reports/reports_base.html"
    title = "Отчёт 2100 - Штаты организации"
    form_class = DateRangeInputForm
    permission_required = ()
    reverse_name = "report_2100"

    def get_success_url(self):
        return reverse(self.reverse_name)

class Report2120View(UnfoldModelAdminViewMixin, FormView):
    template_name = "reports/reports_base.html"
    title = "Отчёт 2120 - Контингенты дома ребёнка"
    form_class = DateRangeInputForm
    permission_required = ()
    reverse_name = "report_2120"

    def get_success_url(self):
        return reverse(self.reverse_name)

    def post(self, request, *args, **kwargs):
        form = DateRangeInputForm(request.POST)
        if form.is_valid():
            report_file_name = build_report_2120(form.cleaned_data['start'], form.cleaned_data['end'])
            return FileResponse(open(report_file_name, 'rb'), as_attachment=True, filename=f'{self.title}.xlsx')
        else:
            return HttpResponseRedirect('#')


class Report2140View(UnfoldModelAdminViewMixin, FormView):
    template_name = "reports/reports_base.html"
    title = "Отчёт 2140 - Движение контингентов дома ребёнка"
    form_class = DateRangeInputForm
    permission_required = ()
    reverse_name = "report_2140"

    def get_success_url(self):
        return reverse(self.reverse_name)

class Report2145View(UnfoldModelAdminViewMixin, FormView):
    template_name = "reports/reports_base.html"
    title = "Отчёт 2145 - Профилактические осмотры детей и их результаты"
    form_class = DateRangeInputForm
    permission_required = ()
    reverse_name = 'report_2145'

    def get_success_url(self):
        return reverse(self.reverse_name)

class Report2146View(UnfoldModelAdminViewMixin, FormView):
    template_name = "reports/reports_base.html"
    title = "Отчёт 2146 - Работа с контингентами детей, находящихся в доме ребёнка"
    form_class = DateRangeInputForm
    permission_required = ()
    reverse_name = 'report_2146'

    def get_success_url(self):
        return reverse(self.reverse_name)

class Report2150View(UnfoldModelAdminViewMixin, FormView):
    template_name = "reports/reports_base.html"
    title = "Отчёт 2150 - Заболеваемость детей"
    form_class = DateRangeInputForm
    permission_required = ()
    reverse_name = 'report_2150'

    def get_success_url(self):
        return reverse(self.reverse_name)
