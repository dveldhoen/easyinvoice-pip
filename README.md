<h1 align="center">Easy Invoice</h1>
<p align="center">A product by<br/><br/><a href="https://budgetinvoice.com" target="_blank" rel="noopener noreferrer"><img width="250" src="https://public.budgetinvoice.com/img/logo_en_original.png" alt="Easy Invoice logo"></a></p>

<h4 align="center">Build for Web and Backend 💪</h4>
<br/>
<p align="center">
  <a href="https://www.npmjs.com/package/easyinvoice"><img src="https://img.shields.io/pypi/v/easyinvoice.svg" alt="Version"></a>
  <a href="https://github.com/dveldhoen/easyinvoice/actions?query=branch%3Amaster"><img src="https://github.com/dveldhoen/easyinvoice/workflows/build/badge.svg" alt="Build Status"></a>
  <a href="https://codecov.io/github/dveldhoen/easyinvoice"><img src="https://img.shields.io/codecov/c/github/dveldhoen/easyinvoice/master.svg" alt="Coverage Status"></a>  
  <br/>
  <a href="https://npmcharts.com/compare/easyinvoice?minimal=true"><img src="https://img.shields.io/pypi/dm/easyinvoice.svg" alt="Downloads"></a>
  <a href="https://www.npmjs.com/package/easyinvoice"><img src="https://img.shields.io/npm/l/easyinvoice.svg" alt="License"></a>
  <a href="https://github.com/dveldhoen/easyinvoice"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="Pull Request's Welcome"></a>
</p>

<p align="center">
<a href="https://apple.co/3ySZ5JY"><img height="45" src="https://public.budgetinvoice.com/img/appstore-badges/apple-appstore-us.png" alt=""/></a>
<a href="https://play.google.com/store/apps/details?id=nl.dashweb.factuursimpel"><img height="45" src="https://public.budgetinvoice.com/img/appstore-badges/google-play-us.png" alt=""/></a>
</p>

<p align="center">
If this package helped you out please star us on Github!
<br/>
Much appreciated!
<br/>
<br/>
<a href="https://github.com/dveldhoen/easyinvoice-pip/"><img src="https://img.shields.io/github/stars/dveldhoen/easyinvoice-pip.svg?style=social&label=Star" alt="Pull Request's Welcome"></a>
</p>

## Important

1. Please note that this package is a wrapper for an API, so it's logic runs on external servers.
2. Your data is secure and will not be shared with third parties.
3. We try to keep the API up and running at all times, but we cannot guarantee 100% uptime. Please build in a retry
   mechanism in case the API is down for maintenance.

## Installing

Using PIP:

```bash
$ pip install easyinvoice
```

Using PIP3:

```bash
$ pip3 install easyinvoice
```

## Platform support

| <b>Platform</b> | Repository | Supported | Link                                                                                                                                                                     |
|-----------------|------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PHP             | Composer   | Yes!      | <a href="https://packagist.org/packages/easyapis.io/easyinvoice"><img src="https://img.shields.io/badge/EasyInvoice%20on-Composer-blue" alt="Available on Composer"></a> |
| Javascript      | NPM        | Yes!      | <a href="https://www.npmjs.com/package/easyinvoice"><img src="https://img.shields.io/badge/EasyInvoice%20on-NPM-blue" alt="Available on NPM"></a>                        |
| Python          | PIP        | Yes!      | <a href="https://pypi.org/project/easyinvoice/"><img src="https://img.shields.io/badge/EasyInvoice%20on-PIP-blue" alt="Available on PIP"></a>                            |
<br/>

## Sample

<br/>
<div align="center">
    <img width="350" style="border: 1px black solid" src="https://public.budgetinvoice.com/img/sample-invoice.png" alt="Easy Invoice Sample Logo Only">
    <img width="350" style="border: 1px black solid" src="https://public.budgetinvoice.com/img/sample-invoice-background.png" alt="Easy Invoice Sample With Background">
</div>

### JSON Configs used for above samples:

- <a href="https://public.budgetinvoice.com/json/easyinvoice-sample.json">[View JSON] First Sample</a>
- <a href="https://public.budgetinvoice.com/json/easyinvoice-sample-background.json">[View JSON] Second Sample</a>
  <br/>

  <br/>

## Plans

| <b>Plan</b> | Rate                  | Price                                                                                                  | Link                                                                                                                                                                   |
|-------------|-----------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Free        | 25 invoices / 15 days | $0                                                                                                     | Not required to register                                                                                                                                               |
| Paid        | Unlimited             | - 30 day free trial<br/>- 1st month $1.99<br/>- $17.99 per month<br/><small>*Prices include VAT<small> | <a href="https://app.budgetinvoice.com/register" target="_blank"><img src="https://img.shields.io/badge/Register%20on-budgetinvoice.com-blue" alt="Register here"></a> |

<br/>

## To use paid

1. Register through:
    - Web: <a href="https://app.budgetinvoice.com/register" target="_blank">https://app.budgetinvoice.com/register</a>
    - iOS: https://apple.co/3ySZ5JY
    - Android: https://play.google.com/store/apps/details?id=nl.dashweb.factuursimpel
2. Create an API key through the app: settings -> API keys
3. Use the API Key as shown in the complete example below. Add the apiKey property to the data object.

Note: The GUI is not (yet) fully translated to English, though the path to getting an apiKey should mostly be in
English. Also this will allow you to use the in app purchase mechanism to pay for the subscription.
<br/>

## Development mode

When using the free version, you can set the mode to 'development' to make sure you are not running into rate limits
while testing this package or developing your invoices. The free version is limited to 25 invoices per 15 days. When
your
invoice looks good, you can switch to 'production' mode to create your production invoices. Production mode is activated
by either not setting the mode or setting the mode to 'production'.

## Direct REST API access

In case you don't want to use NPM, but you want to call our invoice creation api directly.

```shell
# HTTPS POST 
https://api.budgetinvoice.com/v2/free/invoices

# POST Data
Format: JSON
Structure: {
  "data": { # Parent parameter must be 'data'
    "mode": "development", # Production or development, defaults to production
    "products": [
      {
        "quantity": 2,
        "description": "Test product",
        "taxRate": 6,
        "price": 33.87
      }
    ],
  }
} 

# Optionally add your paid apiKey to the header 
Header: "Authorization": "Bearer 123abc" # Please register to receive a production apiKey: https://app.budgetinvoice.com/register
```

## Import

```python
# Import the EasyInvoice library
from easyinvoice import EasyInvoice
```

## Getting Started - Basic Example

```python
# Import the EasyInvoice library
from easyinvoice import EasyInvoice

# Create a dictionary with the settings to create the invoice
data = {
    "apiKey": "free", # Please register to receive a production apiKey: https://app.budgetinvoice.com/register
    "mode": "development", # Production or development, defaults to production
    "products": [
        {
            "quantity": 2,
            "description": "Test product",
            "taxRate": 6,
            "price": 33.87
        }
    ]
}

# This will return the PDF as base64 string
result = EasyInvoice.create(data)

# To save the PDF locally call the save function
EasyInvoice.save(result["pdf"])
```

## High volumes: asynchronous invoice creation
```python
import asyncio
from easyinvoice import EasyInvoice
import asyncio

async def create_invoice_async():
    data = {
        "apiKey": "free",
        "mode": "development",
        "products": [
            {
                "quantity": 2,
                "description": "Test product",
                "taxRate": 6,
                "price": 33.87
            }
        ]
    }
    # Use asyncio.to_thread to run the synchronous EasyInvoice.create in a separate thread
    result = await asyncio.to_thread(EasyInvoice.create, data)
    return result["pdf"]

async def main():
    # Schedule asynchronous execution of create_invoice_async for multiple invoices
    tasks = [create_invoice_async() for _ in range(25)]
    invoices = await asyncio.gather(*tasks)
    return invoices

if __name__ == "__main__":
    all_invoices = asyncio.run(main())
    print(all_invoices)
```

## Full Example

```python
# Import the EasyInvoice library
from easyinvoice import EasyInvoice

# Data will contain all the information we would like to see on our invoice
data = {
    "apiKey": "free", # Please register to receive a production apiKey: https://app.budgetinvoice.com/register
    "mode": "development", # Production or development, defaults to production    
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
        "dueDate": "31-12-2021"
    },
    # The products you would like to see on your invoice
    # Total values are being calculated automatically
    "products": [
        {
            "quantity": 2,
            "description": "Test2",
            "taxRate": 6,
            "price": 33.87
        },
        {
            "quantity": 4.1,
            "description": "Test1",
            "taxRate": 6,
            "price": 12.34
        },
        {
            "quantity": 4.5678,
            "description": "Test2",
            "taxRate": 21,
            "price": 6324.453456
        }
    ],
    # The message you would like to display on the bottom of your invoice
    "bottomNotice": "Kindly pay your invoice within 15 days.",
    # Settings to customize your invoice
    "settings": {
        "currency": "USD", # See documentation 'Locales and Currency' for more info. Leave empty for no currency.
        #     "locale": "nl-NL", # Defaults to en-US, used for number formatting (See documentation 'Locales and Currency')
        #     "margin-top": 25, # Defaults to '25'
        #     "margin-right": 25, # Defaults to '25'
        #     "margin-left": 25, # Defaults to '25'
        #     "margin-bottom": 25, # Defaults to '25'
        #     "format": "A4", # Defaults to A4, options: A3, A4, A5, Legal, Letter, Tabloid
        #     "height": "1000px", // allowed units: mm, cm, in, px
        #     "width": "500px", // allowed units: mm, cm, in, px
        #     "orientation": "landscape" // portrait or landscape, defaults to portrait   
    },
    # Translate your invoice to your preferred language
    "translate": {
        #     "invoice": "FACTUUR",  # Default to 'INVOICE'
        #     "number": "Nummer", # Defaults to 'Number'
        #     "date": "Datum", # Default to 'Date'
        #     "dueDate": "Verloopdatum", # Defaults to 'Due Date'
        #     "subtotal": "Subtotaal", # Defaults to 'Subtotal'
        #     "products": "Producten", # Defaults to 'Products'
        #     "quantity": "Aantal", # Default to 'Quantity'
        #     "price": "Prijs", # Defaults to 'Price'
        #     "productTotal": "Totaal", # Defaults to 'Total'
        #     "total": "Totaal", # Defaults to 'Total'
        #     "taxNotation": "btw" // Defaults to 'vat'
    },
    # Customize enables you to provide your own templates
    # Please review the documentation for instructions and examples
    # "customize": {
    #  "template": "SGVsbG8gd29ybGQh" // Must be base64 encoded html. This example contains 'Hello World!' in base64  
    # },
}

# Returns a dict containing all the data of the invoice
result = EasyInvoice.create(data)

# Store the pdf locally
EasyInvoice.save(result["pdf"], 'myInvoice')
```

## Return values

| <b>Key</b>                                          | Value                                                                | Data Type     |
|-----------------------------------------------------|----------------------------------------------------------------------|---------------|
| <b>result["pdf"]</b>                                | <b>The PDF file as base64 string</b>                                 | <b>String</b> |
| result["calculations"]["products"]                  | Array of the products used in creation                               | Array         |
| result["calculations"]["products"][key]["subtotal"] | Rounded price without tax per product                                | Number        |
| result["calculations"]["products"][key]["tax"]      | Rounded tax per product                                              | Number        |
| result["calculations"]["products"][key]["total"]    | Rounded price including tax per product                              | Number        |
| result["calculations"]["tax"]                       | Array of objects containing total calculated tax per unique tax rate | Array         |
| result["calculations"]["tax"][rate]                 | Total tax for all products with same tax rate                        | Number        |
| result["calculations"]["subtotal"]                  | Rounded price without tax for all products                           | Number        |
| result["calculations"]["total"]                     | Rounded price without tax for all products                           | Number        |

## Error handling

```python
try:
    # Import the EasyInvoice library
    from easyinvoice import EasyInvoice
    
    # Create a dictionary with the settings to create the invoice
    data = {
        "apiKey": "free", # Please register to receive a production apiKey: https://app.budgetinvoice.com/register
        "mode": "development", # Production or development, defaults to production
        "products": [
            {
                "quantity": 2,
                "description": "Test product",
                "taxRate": 6,
                "price": 33.87
            }
        ]
    }
    
    # Returns a dict containing all the data of the invoice
    result = EasyInvoice.create(data)

    # Store the pdf locally
    EasyInvoice.save(result["pdf"], 'invoice')
except Exception as e:
    # If an error occurs, it will be caught here
    print(e)
```

## Locales and Currency

Used for number formatting and the currency symbol:

```python
# E.g. for Germany, prices would look like 123.456,78 €
data = {
    "apiKey": "free", # Please register to receive a production apiKey: https://app.budgetinvoice.com/register
    "mode": "development", # Production or development, defaults to production
    "settings":
        {
            "locale": "de-DE",
            "currency": "EUR"
        }
}

# E.g. for US, prices would look like $123,456.78
data = {
    "apiKey": "free", # Please register to receive a production apiKey: https://app.budgetinvoice.com/register
    "mode": "development", # Production or development, defaults to production
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

## Template customization

Download our default template (invoice-v2) <a href="https://public.easyinvoice.cloud/templates/invoice-v2/index.txt" download>here</a> to have an example which you can customize.

Supported file types:

- Base64
- URL (soon)

```python
# You are able to provide your own html template
html = "<p>Hello world! This is invoice number %number%</p>"

data = {
    "customize": {
        # Your template needs to be base64 encoded
        "template": base64.b64encode(html)
    },
    "settings": {
        "number": '2022.0001'
    }
}

EasyInvoice.create(data)

# This will return a pdf with the following content
# Hello world! This is invoice number 2022.0001
```

### Variable placeholders
The following placeholders can be put into your template. They will be replaced by their corresponding value upon creation.

<table>
<tr>
<td><b>Placeholder</b></td> 
<td><b>Will be replaced by</b></td>
</tr>
<tr>
<td>%document-title%</td> 
<td>translate.invoice</td>
</tr>
<tr>
<td>%logo%</td> 
<td>images.logo</td>
</tr>
<tr>
<td>%company-from%</td> 
<td>sender.company</td>
</tr>
<tr>
<td>%address-from%	</td> 
<td>sender.address</td>
</tr>
<tr>
<td>%zip-from%	</td> 
<td>sender.zip</td>
</tr>
<tr>
<td>%city-from%</td> 
<td>sender.city</td>
</tr>
<tr>
<td>%country-from%</td> 
<td>sender.country</td>
</tr>
<tr>
<td>%sender-custom-1%</td> 
<td>sender.custom1</td>
</tr>
<tr>
<td>%sender-custom-2%</td> 
<td>sender.custom2</td>
</tr>
<tr>
<td>%sender-custom-3%</td> 
<td>sender.custom3</td>
</tr>
<tr>
<td>%company-to%</td> 
<td>client.company</td>
</tr>
<tr>
<td>%address-to%	</td> 
<td>client.address</td>
</tr>
<tr>
<td>%zip-to%	</td> 
<td>client.zip</td>
</tr>
<tr>
<td>%city-to%</td> 
<td>client.city</td>
</tr>
<tr>
<td>%country-to%</td> 
<td>client.country</td>
</tr>
<tr>
<td>%client-custom-1%</td> 
<td>client.custom1</td>
</tr>
<tr>
<td>%client-custom-2%</td> 
<td>client.custom2</td>
</tr>
<tr>
<td>%client-custom-3%</td> 
<td>client.custom3</td>
</tr>
<tr>
<td>%number-title%</td> 
<td>translate.number</td>
</tr>
<tr>
<td>%number%</td> 
<td>settings.number</td>
</tr>
<tr>
<td>%date-title%</td> 
<td>translate.date</td>
</tr>
<tr>
<td>%date%</td> 
<td>settings.date</td>
</tr>
<tr>
<td>%due-date-title%</td> 
<td>translate.dueDate</td>
</tr>
<tr>
<td>%due-date%</td> 
<td>settings.dueDate</td>
</tr>
<tr>
<td>%products-header-products%</td> 
<td>translate.products</td>
</tr>
<tr>
<td>%products-header-quantity%</td> 
<td>translate.quantity</td>
</tr>
<tr>
<td>%products-header-price%</td> 
<td>translate.price</td>
</tr>
<tr>
<td>%products-header-total%</td> 
<td>translate.productTotal</td>
</tr>
<tr>
<td>
A custom product row must be enclosed in products tags like:

```html
<products>
    <!-- Product row html -->
</products>
```
Don't leave out the product tags or your custom product row won't be iterable by the template parser and you will end up with a single product row. Customize the html as you wish.
</td>
<td>products</td>
</tr>
<tr>
<td>

```html
Within: <products></products>
```

%description%
</td> 
<td>products[].description</td>
</tr>
<tr>
<td>

```html
Within: <products></products>
```

%quantity%
</td>  
<td>products[].quantity</td>
</tr>
<tr>
<td>

```html
Within: <products></products>
```

%price%
</td>   
<td>products[].price</td>
</tr>
<tr>
<td>

```html
Within: <products></products>
```

%row-total%
</td>    
<td>products[].quantity * products[].price (rounded)</td>
</tr>
<tr>
<td>%subtotal-title%</td> 
<td>translate.subtotal</td>
</tr>
<tr>
<td>%subtotal%</td> 
<td><b>Auto inserted:</b>
<br/>
Calculated total price excluding tax</td>
</tr>
<tr>
<td>
A custom tax row must be enclosed in tax tags like:

```html
<tax>
    <!-- Tax row html -->
</tax>
```
Don't leave out the tax tags or your custom tax row won't be iterable by the template parser and you will end up with a single tax row. Customize the html as you wish.
</td>
<td>tax</td>
</tr>
<tr>
<td>

```html
Within: <tax></tax>
```

%tax-notation%
</td>    
<td>settings.taxNotation</td>
</tr>
<tr>
<td>

```html
Within: <tax></tax>
```

%tax-rate%
</td>    
<td><b>Auto inserted:</b><br/>
Distinct tax rate used in products</td>
</tr>
<tr>
<td>

```html
Within: <tax></tax>
```

%tax%
</td>    
<td><b>Auto inserted:</b><br/>
Calculated total tax for rate</td>
</tr>
<tr>
<td>%total%</td>    
<td><b>Auto inserted:</b><br/>
Calculated total price including tax</td>
</tr>
</table>