from django.urls import path
from phonebook import views


app_name = 'phonebook'

urlpatterns = [
    path('list', views.ContatoList.as_view(), name = 'list'),
]
