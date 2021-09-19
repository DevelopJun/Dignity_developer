from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("여기가 Category main 파일 시작 부분입니다.")
