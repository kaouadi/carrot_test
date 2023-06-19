from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.my_html_file, name='home'),

]


handler404 = 'core.views.page_not_found'