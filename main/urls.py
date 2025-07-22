from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/', views.exact_catalog, name='exact_catalog'),
    path('zayavka/', views.request_form, name='request_form'), 
]