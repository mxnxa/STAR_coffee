from django.shortcuts import render
from .models import History

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def about(request):
    return render(request, 'pages/company_info.html')

def history(request):
    history_list = History.objects.order_by('-year')
    context = {'history_list': history_list}
    return render(request, 'pages/company_history.html', context)

def contact(request):
    return render(request, 'pages/contact.html')
