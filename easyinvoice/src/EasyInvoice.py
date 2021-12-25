import base64
import json
import requests


class EasyInvoice:

    @staticmethod
    def create(data):
        url = "https://api.easyinvoice.cloud/v2/free/invoices"
        data = {
            "data": data
        }
        response = requests.post(url, json=data)
        result = response.json()
        return result["data"]

    @staticmethod
    def save(invoice_base64, filename="invoice"):
        with open(filename + ".pdf", 'wb') as file:
            file.write(base64.b64decode(invoice_base64))
