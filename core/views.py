import sys
from inspect import isclass

from django.http import FileResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, TemplateView
from unfold.views import UnfoldModelAdminViewMixin

from core.forms import DateRangeInputForm, FileInputForm
from core.reports import build_report_summary
from core.uploads import upload_2145, upload_2146


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
            if item[0].startswith('Report') and isclass(item[1]) and issubclass(item[1], FormView) and issubclass(item[1], UnfoldModelAdminViewMixin):
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

class Upload2145View(UnfoldModelAdminViewMixin, FormView):
    template_name = "upload/upload_base.html"
    title = "Загрузка результатов профилактической работы с детьми"
    form_class = FileInputForm
    permission_required = ()
    reverse_name = 'upload_2145'

    def post(self, request, *args, **kwargs):
        form = FileInputForm(request.POST, request.FILES)
        if form.is_valid():
            upload_2145(request.FILES["file"])
            return HttpResponseRedirect('#success')
        else:
            return HttpResponseRedirect('#error')

class Upload2146View(UnfoldModelAdminViewMixin, FormView):
    template_name = "upload/upload_base.html"
    title = "Загрузка данных по работе с контингентами"
    form_class = FileInputForm
    permission_required = ()
    reverse_name = 'upload_2146'

    def post(self, request, *args, **kwargs):
        form = FileInputForm(request.POST, request.FILES)
        if form.is_valid():
            upload_2146(request.FILES["file"])
            return HttpResponseRedirect('#success')
        else:
            return HttpResponseRedirect('#error')
