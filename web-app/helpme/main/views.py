from django.shortcuts import render
from .templates.repository.dp_service import *
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def result(request):
    line = 'Скорее всего, Вы получите "Отлично"!\nИ это ожидаемо, ведь Вы, кажется, трудились весь семестр, не покладая рук.\nНе бросайте начатое, осталось совсем чуть-чуть, и у Вас обязательно все получится!\nВ Вас верит создатель этого сайта, и статистика также на вашей стороне!'
    data = {'result': line}
    return render(request, 'main/result_page.html', data)

def dbases(request):
    return render(request, 'main/dbases.html')

def avgrade(request):
    service = DPService()
    result = service.get_av_grade()
    data = {'result': result}
    return render(request, 'main/avgrade.html', data)

def reccount(request):
    service = DPService()
    result = service.get_data_count()
    data = {'result': result}
    return render(request, 'main/reccount.html', data)

def srcfiles(request):
    service = DPService()
    result = service.get_source_files()
    data = {'result': result}
    return render(request, 'main/processed.html', data)


