from lib2to3.fixes.fix_input import context

from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "reports/index.html", context)