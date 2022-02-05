from django.urls import path

from . import views
app_name = 'api'

urlpatterns = [
    path('',views.index, name="index"),
    path('create/doctor/',views.create_doctor, name="create-doc"),
    path('create/appt/',views.create_appt, name="create-appt"),
    path('display-all',views.get_all_doctors, name="display-all"),
    path('display/<int:record_id>',views.get_select_doctor, name="display"),
    path('delete/<int:appt_id>',views.delete_appt, name="delete"),
]
