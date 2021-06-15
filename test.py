from easyinvoice.src.EasyInvoice import EasyInvoice

# Returns a base64 string containing the invoice as PDF
pdfdata = EasyInvoice.create({})

# Store the pdf locally
EasyInvoice.save(pdfdata, 'invoice.pdf')
