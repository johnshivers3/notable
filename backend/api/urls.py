from django.urls import path

from . import views
app_name = 'api'

urlpatterns = [
    path('',views.index, name="index"),
    path('create',views.create_record, name="create"),
    path('display-all',views.get_all_records, name="display-all"),
    path('display/<int:record_id>',views.get_select_records, name="display"),
    path('update/<int:record_id>',views.update_record, name="update"),
    path('delete/<int:record_id>',views.delete_record, name="delete"),
]
