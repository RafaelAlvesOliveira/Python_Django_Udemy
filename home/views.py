from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    print('HOME')
    return HttpResponse('HOME do app')
