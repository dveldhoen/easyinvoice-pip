<p align="center"><a href="https://easyinvoice.cloud" target="_blank" rel="noopener noreferrer"><img width="250" src="https://public.easyinvoice.cloud/img/logo_en_original.png" alt="Easy Invoice logo"></a></p>

<p align="center">Easy Invoice is a package that will help you to create beautiful PDF invoices with ease.</p>


<p align="center">
If this package helped you out please star us on Github!
<br/>
Much appreciated!
<br/>
<br/>
<a href="https://github.com/dveldhoen/easyinvoice-pip/"><img src="https://img.shields.io/github/stars/dveldhoen/easyinvoice-pip.svg?style=social&label=Star" alt="Pull Request's Welcome"></a>
</p>

## Platform support

|<b>Platform</b> | Repository |Supported  | Link |
|---|---|---|---|
| PHP | Composer |Yes! | <a href="https://packagist.org/packages/easyapis.io/easyinvoice"><img src="https://img.shields.io/badge/EasyInvoice%20on-Composer-blue" alt="Available on Composer"></a> |
| Javascript | NPM | Yes! | <a href="https://www.npmjs.com/package/easyinvoice"><img src="https://img.shields.io/badge/EasyInvoice%20on-NPM-blue" alt="Available on NPM"></a> |
| Python | PIP | Yes! | <a href="https://pypi.org/project/easyinvoice/"><img src="https://img.shields.io/badge/EasyInvoice%20on-PIP-blue" alt="Available on PIP"></a> |
| Java | Maven | In progress... |  |

## Sample

<div align="center">
    <img width="350" style="border: 1px black solid" src="https://public.easyinvoice.cloud/img/sample-invoice.png" alt="Easy Invoice Sample Logo Only">
    <img width="350" style="border: 1px black solid" src="https://public.easyinvoice.cloud/img/sample-invoice-background.png" alt="Easy Invoice Sample With Background">
</div>

### JSON Configs used for above samples:

- <a href="https://public.easyinvoice.cloud/json/easyinvoice-sample.json">[View JSON] First Sample</a>
- <a href="https://public.easyinvoice.cloud/json/easyinvoice-sample-background.json">[View JSON] Second Sample</a>


## Installing

Using PIP:

```bash
$ pip install easyinvoice
```

Using PIP3:

```bash
$ pip3 install easyinvoice
```

## Getting Started - Basic Example

```python
# Import the EasyInvoice library
from easyinvoice import EasyInvoice

# This will return the PDF as base64 string
result = EasyInvoice.create({})

# To save the PDF locally call the save function
EasyInvoice.save(result.pdf)
```

## Full Example

```python
# Import the EasyInvoice library
from easyinvoice import EasyInvoice

# Data will contain all the information we would like to see on our invoice
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
        "currency": "USD", # See documentation 'Locales and Currency' for more info. Leave empty for no currency.
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
EasyInvoice.save(pdfdata, 'invoice.pdf')
```

## Locales and Currency

Used for number formatting and the currency symbol:

```python
# E.g. for Germany, prices would look like 123.456,78 €
data = {
    "settings":
        {
            "locale": "de-DE",
            "currency": "EUR"
        }
}

# E.g. for US, prices would look like $123,456.78
data = {
    "settings":
        {
            "locale": "en-US",
            "currency": "USD"
        }
}
```

Formatting and symbols are applied through
the [ECMAScript Internationalization API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)

[Click here for a list of locale codes](https://datahub.io/core/language-codes/r/3.html)
<br/>
[Click here for a list of currency codes](https://www.iban.com/currency-codes)

Disclaimer: Not all locales and currency codes found in the above lists might be supported by the ECMAScript
Internationalization API.

## Logo and Background

The logo and url inputs accept either a URL or a base64 encoded file.

Supported file types:

- Logo: image
- Background: image, pdf

### URL

```python
data = {
    "images": {
        "logo": "https://public.easyinvoice.cloud/img/logo_en_original.png",
        "background": "https://public.easyinvoice.cloud/img/watermark_draft.jpg"
    }
}
```

### Base64

```python
data = {
    # Note: Sample base64 string
    # Please use the link below to convert your image to base64
    "images": {
        "logo": "iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",
        "background": "iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="
    }
}
```

[Click here for an online tool to convert an image to base64](https://base64.guru/converter/encode/image)

## View PDF

You could view your base64 pdf through the following website:
https://base64.guru/converter/decode/pdf

Paste the base64 string and click 'Decode Base64 to PDF'.