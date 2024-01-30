import base64
import requests

class EasyInvoice:

    @staticmethod
    def create(data):
        try:
            url = "https://api.easyinvoice.cloud/v2/free/invoices"
            data = {
                "data": data
            }
            response = requests.post(url, json=data)
            if response.status_code == 200:
                result = response.json()
                return result["data"]
            else:
                raise SystemExit(response.json())
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

    @staticmethod
    def save(invoice_base64, filename="invoice"):
        try:
            with open(filename + ".pdf", 'wb') as file:
                file.write(base64.b64decode(invoice_base64))
        except Exception as e:
            raise SystemExit(e)


