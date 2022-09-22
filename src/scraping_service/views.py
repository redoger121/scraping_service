from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    date=datetime.datetime.now().date()
    name='Dave'
    context={'date':date, 'name':name}
    return render(request, 'base.html', context)