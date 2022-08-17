import pdfplumber
import requests


def get_pdf_from_url(url):
    local_filename = url.split('/')[-1]
#     print(local_filename)
    with requests.get(url) as r:
        with open(local_filename, 'wb') as f:
            f.write(r.content)
    return local_filename


def get_balance_Enel_electricity(pdf):
        with pdfplumber.open(pdf) as pdf:
            page = pdf.pages[0]
            text = page.extract_text()
        for row in text.split("\n"):
            if row.startswith("Total de plata"):
                balance = float(row.split(" ")[-2].replace(",", "."))
                return balance



# test_link = "http://127.0.0.1:8000/media/Fee/UtilityBill/42005385322_1.pdf"
#
# print(get_pdf_from_url(test_link))
