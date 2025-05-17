from datetime import date

from django import forms
from unfold.widgets import UnfoldAdminDateWidget, UnfoldAdminFileFieldWidget


class DateRangeInputForm(forms.Form):
    start = forms.DateField(
        label="Начало отчётного периода",
        required=True,
        widget=UnfoldAdminDateWidget,
    )
    end = forms.DateField(
        label="Конец отчётного периода",
        required=True,
        widget=UnfoldAdminDateWidget,
    )

    class Media:
        js = [
            "admin/js/vendor/jquery/jquery.js",
            "admin/js/jquery.init.js",
            "admin/js/calendar.js",
            "admin/js/admin/DateTimeShortcuts.js",
            "admin/js/core.js",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start'].initial = date(date.today().year - 1, 1, 1)
        self.fields['end'].initial = date(date.today().year - 1, 12, 31)

class FileInputForm(forms.Form):
    file = forms.FileField(label="Файл с данными",
                           allow_empty_file=True,
                           required=True,
                           widget=UnfoldAdminFileFieldWidget)
    class Media:
        js = [
            "admin/js/vendor/jquery/jquery.js",
            "admin/js/jquery.init.js",
            "admin/js/calendar.js",
            "admin/js/admin/DateTimeShortcuts.js",
            "admin/js/core.js",
        ]
