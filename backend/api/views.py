from datetime import datetime
from pprint import pprint
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.decorators.http import require_http_methods
from .models import Record, Record_Data
from .forms import RecordForm, RecordDataForm

@require_http_methods(["GET"])
def index(request):
    return HttpResponse("Hello, world!")


@require_http_methods(["GET"])
def get_all_records(request):
    record_list = get_list_or_404(Record.objects.order_by("-record_date"))
    template = loader.get_template("api_template/index.html")
    formatted_record_list = [
        {
            "id": record.id,
            "name": record.record_name,
            "date": record.record_date,
        }
        for record in record_list
    ]
    context = {"latest_record_list": formatted_record_list}
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def get_select_records(request, record_id):
    select_record = get_object_or_404(Record, pk=record_id)
    select_record = dict(
        id=select_record.id,
        name=select_record.record_name,
        date=select_record.record_date,
    )
    template = loader.get_template("api_template/index.html")
    context = {"latest_record_list": [select_record]}

    return HttpResponse(template.render(context, request))


@require_http_methods(["POST"])
def create_record(request):
    new_record = RecordForm(request.POST)

    new_record.save()

    return HttpResponse("create_record")

@require_http_methods(["PUT"])
def update_record(request, record_id):
    
    return HttpResponse("update_record")


@require_http_methods(["GET","DELETE"])
def delete_record(request, record_id):

    try:
        select_record = get_object_or_404(Record, pk=record_id)
        select_record.delete()
        return HttpResponse(f"deleted record : {record_id}")
    except:
        return HttpResponse(f"could not delete record : {record_id}")
