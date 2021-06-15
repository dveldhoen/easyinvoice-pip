import base64
from easyinvoice.src.EasyInvoice import EasyInvoice

data = {
    # Defaults to INVOICE
    "documentTitle": "RECEIPT",

    # Defaults to en-US, used for number formatting (see docs)
    # "locale": "de-DE",

    # See documentation 'Locales and Currency' for more info
    "currency": "USD",

    # or e.g. gst
    "taxNotation": "vat",
    "marginTop": 25,
    "marginRight": 25,
    "marginLeft": 25,
    "marginBottom": 25,

    # Use url or base64
    "logo": "https://public.easyinvoice.cloud/img/logo_en_original.png",
    # Use url or base64
    "background": "https://public.easyinvoice.cloud/img/watermark-draft.jpg",

    "sender": {
        "company": "Sample Corp",
        "address": "Sample Street 123",
        "zip": "1234 AB",
        "city": "Sampletown",
        "country": "Samplecountry"
        # "custom1": "custom value 1",
        # "custom2": "custom value 2",
        # "custom3": "custom value 3"
    },
    "client": {
        "company": "Client Corp",
        "address": "Clientstreet 456",
        "zip": "4567 CD",
        "city": "Clientcity",
        "country": "Clientcountry"
        # "custom1": "custom value 1",
        # "custom2": "custom value 2",
        # "custom3": "custom value 3"
    },
    "invoiceNumber": "2021.0001",
    "invoiceDate": "1.1.2021",
    "products": [
        {
            "quantity": "2",
            "description": "Test1",
            "tax": 6,
            "price": 33.87
        },
        {
            "quantity": "4",
            "description": "Test2",
            "tax": 21,
            "price": 10.45
        }
    ],
    "bottomNotice": "Kindly pay your invoice within 15 days.",
    # Used for translating the headers to your preferred language
    # Defaults to English. Below example is translated to Dutch
    # "translate": {
    #     "invoiceNumber": "Factuurnummer",
    #     "invoiceDate": "Factuurdatum",
    #     "products": "Producten",
    #     "quantity": "Aantal",
    #     "price": "Prijs",
    #     "subtotal": "Subtotaal",
    #     "total": "Totaal"
    # }
}

# Returns a base64 string containing the invoice as PDF
pdfdata = EasyInvoice.create(data)

# Store the pdf locally
EasyInvoice.save(pdfdata, 'invoice')
