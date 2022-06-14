from django.urls import path
from utility_bills.views import bill_file_list

urlpatterns = [
    path('', bill_file_list, name='bill-file-list')
]