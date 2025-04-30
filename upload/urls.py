from django.urls import path

from upload import views

app_name = 'uploads'

urlpatterns = [
    path('', views.index, name='index'),
]