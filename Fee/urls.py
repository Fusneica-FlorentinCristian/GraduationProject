from django.urls import path
from Fee.views import utility_bill_file_list

urlpatterns = [
    path('', utility_bill_file_list, name='utility-bill-file-list')
]