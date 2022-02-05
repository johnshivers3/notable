from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def create_record(request):
    return HttpResponse("create_record")

def get_all_records(request):
    return HttpResponse("get_all_records")

def get_select_records(request):
    return HttpResponse("get_select_records")

def update_record(request):
    return HttpResponse("update_record")

def delete_record(request):
    return HttpResponse("delete_record")
