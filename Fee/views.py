# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from Fee.models import UtilityBill
from Fee.forms import DocumentForm


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def utility_bill_file_list(request):
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # payee = User.objects.filter(username__startswith="tenant")[0]
            # print(payee.id)
            some_bill = UtilityBill.objects.first()
            some_bill.file = request.FILES['docfile']
            some_bill.pk = None
            some_bill.save()
            print(some_bill.pk)

            # Redirect to the document list after POST
            return redirect('utility-bill-file-list')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = []
    for bill in UtilityBill.objects.all():
        if bill.file:
            documents.append(bill.file)

    # documents = [bill.file for bill in Bill.objects.all()]

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    # print("!!!!!!!!!!!!!!!!!!!!----------------------------!!!!!!!!!!!!!!!!!!!!!!!" + str(documents[0].url))
    return render(request, 'Fee/utility_bill_file_list.html', context)
