import base64
import json
import requests


class EasyInvoice:

    @staticmethod
    def create(data):
        url = "https://api.easyinvoice.cloud/v1/invoices"
        response = requests.post(url, data)
        result = json.loads(json.dumps(response.json()))
        return result["data"]["pdf"]

    @staticmethod
    def save(invoice_base64, filename="invoice"):
        with open(filename + ".pdf", 'wb') as file:
            file.write(base64.b64decode(invoice_base64))
