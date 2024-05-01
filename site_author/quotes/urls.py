from django.urls import path

from . import views

app_name = "quotes"


urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/<int:id_>/', views.description_auth, name='description_auth'),
    path('add_author/', views.auth_ur, name='auth_ur'),
    path('add_quote/', views.quote_ur, name='quote_ur'),
]
