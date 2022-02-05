from django.urls import path

from . import views

urlpatterns = [
    path('/',views.index, name="index"),
    path('create',views.create_record, name="create"),
    path('display-all',views.get_all_records, name="display-all"),
    path('display',views.get_select_records, name="display"),
    path('update',views.update_record, name="update"),
    path('delete',views.delete_record, name="delete"),
]
