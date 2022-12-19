from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('result', views.result, name = 'result'),
    path('dbases', views.dbases, name = 'dbases'),
    path('dbases/reccount', views.reccount, name = 'reccount'),
    path('dbases/avgrade', views.avgrade, name = 'avgrade'),
    path('dbases/source_files', views.srcfiles, name = 'processed'),

]