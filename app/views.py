from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat1(request):
    return HttpResponse('VIRAT KHOLI BIOGRAPHY')
def virat(request):
    return render(request,'virat.html')
