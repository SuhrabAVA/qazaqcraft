from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/', views.exact_catalog, name='exact_catalog'),
    path('zayavka/', views.request_form, name='request_form'), 
    path(
      'yandex_51274e08aa021645.html',
      TemplateView.as_view(
        template_name='yandex_51274e08aa021645.html',
        content_type='text/html'
      )
    ),
]

urlpatterns += [
    
]
