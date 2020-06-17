from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, DetailView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import functools
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

from django.conf import settings

from django_weasyprint import WeasyTemplateResponseMixin, WeasyTemplateView, WeasyTemplateResponse
from django_weasyprint.views import CONTENT_TYPE_PNG



# Create your views here.
def dashboard(request):
    return render(request, 'NISIInvoice/sample.html')

class AddInvoice(CreateView):
    model = Invoice
    template_name = 'NISIInvoice/invoice_form.html'
    fields = ["first_name", "last_name"]

class InvoiceList(ListView):
    model = Invoice
    template_name = 'NISIInvoice/invoice_list.html'

class InvoiceDetail(DetailView):
    model = Invoice
    template_name = 'NISIInvoice/pdf_template.html'

def InvoicePdf(request, pk):
    Invoice1 = Invoice.objects.get(pk=pk)

    # Rendered
    html_string = render_to_string('NISIInvoice/pdf_template.html', {'Invoice1':Invoice1})
    html = HTML(string=html_string)
    result = html.write_pdf(
        stylesheets=[
        # Change this to suit your css  path
        "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"

    ]
    )

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=Invoice.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.seek(0)
        response.write(output.read())
    return response
