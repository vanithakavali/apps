from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni1(request):
    return HttpResponse('M.S.DHONI BIOGRAPHY')
def dhoni(request):
    return render(request,'dhoni.html')

