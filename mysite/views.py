from django.shortcuts import render
from .models import MainContent

def index(request):
    content_list = MainContent.objects.order_by('pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)

def detail(request):
    return render(request, 'mysite/content_detail.html')

# def files(request):
#     product_img = MainContent.objects.all()
#
#     return render(
#         request,
#         'mysite/content_list.html',
#         {
#             'product_img': product_img
#         }
#     )

# Create your views here.
