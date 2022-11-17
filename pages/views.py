from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def about(request):
    return render(request, 'pages/company_info.html')

def contact(request):
    return render(request, 'pages/contact.html')

# Create your views here.
