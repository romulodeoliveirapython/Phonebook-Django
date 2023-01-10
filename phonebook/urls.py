from django.urls import path
from phonebook import views


app_name = 'phonebook'

urlpatterns = [
    path('list/', views.ContatoList.as_view(), name = 'list'),
    path('create/', views.ContatoCreate.as_view(), name = 'create'),
    path('update/<int:pk>/', views.ContatoUpdate.as_view(), name = 'update'),
]
