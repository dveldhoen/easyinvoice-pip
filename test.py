from easyinvoice.src.EasyInvoice import EasyInvoice

data = {
    "images": {
        # The logo on top of your invoice
        "logo": "https://public.easyinvoice.cloud/img/logo_en_original.png",
        # The invoice background
        "background": "https://public.easyinvoice.cloud/img/watermark-draft.jpg"
    },
    # Your own data
    "sender": {
        "company": "Sample Corp",
        "address": "Sample Street 123",
        "zip": "1234 AB",
        "city": "Sampletown",
        "country": "Samplecountry"
        # "custom1": "sender-custom1",
        # "custom2": "sender-custom2",
        # "custom3": "sender-custom3"
    },
    # Your recipient
    "client": {
        "company": "Client Corp",
        "address": "Clientstreet 456",
        "zip": "4567 CD",
        "city": "Clientcity",
        "country": "Clientcountry"
        # "custom1": "client-custom1",
        # "custom2": "client-custom2",
        # "custom3": "client-custom3"
    },
    "information": {
        # Invoice number
        "number": "2021.0001",
        # Invoice data
        "date": "12-12-2021",
        # Invoice due date
        "due-date": "31-12-2021"
    },
    # The products you would like to see on your invoice
    # Total values are being calculated automatically
    "products": [
        {
            "quantity": 2,
            "description": "Test2",
            "tax-rate": 6,
            "price": 33.87
        },
        {
            "quantity": 4.1,
            "description": "Test1",
            "tax-rate": 6,
            "price": 12.34
        },
        {
            "quantity": 4.5678,
            "description": "Test2",
            "tax-rate": 21,
            "price": 6324.453456
        }
    ],
    # The message you would like to display on the bottom of your invoice
    "bottom-notice": "Kindly pay your invoice within 15 days.",
    "settings": {
        "currency": "USD",  # See documentation 'Locales and Currency' for more info. Leave empty for no currency.
        #     "locale": "nl-NL", # Defaults to en-US, used for number formatting (See documentation 'Locales and Currency')
        #     "tax-notation": "gst", # Defaults to 'vat'
        #     "margin-top": 25, # Defaults to '25'
        #     "margin-right": 25, # Defaults to '25'
        #     "margin-left": 25, # Defaults to '25'
        #     "margin-bottom": 25, # Defaults to '25'
        #     "format": "A4" # Defaults to A4, options: A3, A4, A5, Legal, Letter, Tabloid
    },
    "translate": {
        #     "invoice": "FACTUUR",  # Default to 'INVOICE'
        #     "number": "Nummer", # Defaults to 'Number'
        #     "date": "Datum", # Default to 'Date'
        #     "due-date": "Verloopdatum", # Defaults to 'Due Date'
        #     "subtotal": "Subtotaal", # Defaults to 'Subtotal'
        #     "products": "Producten", # Defaults to 'Products'
        #     "quantity": "Aantal", # Default to 'Quantity'
        #     "price": "Prijs", # Defaults to 'Price'
        #     "product-total": "Totaal", # Defaults to 'Total'
        #     "total": "Totaal" # Defaults to 'Total'
    },
}

# Returns a dict containing all the data of the invoice
pdfdata = EasyInvoice.create(data)

# Store the pdf locally
EasyInvoice.save(pdfdata, 'invoice')
