# -*- coding: utf-8 -*-
from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect

# from Fee.models import UtilityBill
from apps.forms.feeForms import DocumentForm
from apps.models.modelsFee import UtilityBill
from utils.ManipulatePDF.manipulate_pdf import get_balance_Enel_electricity


DEBUG = True


def utility_bill_file_list(request):
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # payee = User.objects.filter(username__startswith="tenant")[0]
            # print(payee.id)
            if DEBUG:
                # getting the property, provider and type from some_bill to add to new_bill
                some_bill = UtilityBill.objects.first()

                new_bill = UtilityBill(deadline=datetime.today() + relativedelta(months=1),
                                       file=request.FILES['docfile'], property=some_bill.property,
                                       provider="Enel", type=some_bill.type)
                new_bill.balance = get_balance_Enel_electricity(pdf=new_bill.file)
                new_bill.save()

                print("Printed--------------------------" + str(new_bill.pk))

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

    # if DEBUG:
    #     for document in documents:
    #         hidro_balance = get_balance_HidroElectrica(document)
    #         print(hidro_balance)

    context = {'documents': documents, 'form': form, 'message': message}
    # Render list page with the documents and the form
    return render(request, 'Fee/utility_bill_file_list.html', context)
