from datetime import datetime
from pprint import pprint
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.decorators.http import require_http_methods
from .models import Doctor, Appt_Data
from .forms import ApptForm

@require_http_methods(["GET"])
def index(request):
    return HttpResponse("Hello, world!")


@require_http_methods(["GET"])
def get_all_doctors(request):
    doctor_list = get_list_or_404(Doctor.objects.order_by("last_name"))
    template = loader.get_template("api_template/index.html")
    formatted_doctor_list = [
        {
            "id": doctor.id,
            "name": doctor.first_name,
            "date": doctor.last_name,
            "email": doctor.email,
        }
        for doctor in doctor_list
    ]
    context = {"latest_doctor_list": formatted_doctor_list}
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def get_select_doctor(request, record_id):
    select_doctor = get_object_or_404(Doctor, pk=record_id)
    select_doctor = dict(
        select_doctor
    )
    template = loader.get_template("api_template/appt.html")
    context = {"latest_doctor_list": [select_doctor]}

    return HttpResponse(template.render(context, request))


@require_http_methods(["POST"])
def create_doctor(request):
    new_record = Doctor(request.POST)

    new_record.save()

    return HttpResponse("Success doc added")
@require_http_methods(["POST"])
def create_appt(request):
    new_record = ApptForm(request.POST)

    new_record.save()

    return HttpResponse("Success appt added")


@require_http_methods(["DELETE"])
def delete_appt(request, appt_id):

    try:
        select_appt = get_object_or_404(Appt_Data, pk=appt_id)
        select_appt.delete()
        return HttpResponse(f"deleted appt : {appt_id}")
    except:
        return HttpResponse(f"could not delete appt : {appt_id}")
