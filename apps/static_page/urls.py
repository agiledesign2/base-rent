from django.urls import include, path, re_path

from .views import home_view, about_view

app_name = 'static_page'

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
]
