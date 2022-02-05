from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Record, Record_Data

def index(request):
    return HttpResponse("Hello, world!")

def create_record(request):
    return HttpResponse("create_record")

def get_all_records(request):
    latest_record_list = Record.objects.order_by("-record_date")
    template = loader.get_template('api_template/index.html')
    latest_record_list = [{'id': record.id, 'name': record.record_name, 'date': record.record_date.strftime("%m-%d-%Y")} for record in latest_record_list]
    context = {"latest_record_list": latest_record_list}

    return HttpResponse(template.render(context, request))

def get_select_records(request, record_id):
    return HttpResponse("get_select_records")

def update_record(request, record_id):
    return HttpResponse("update_record")

def delete_record(request, record_id):
    return HttpResponse("delete_record")
