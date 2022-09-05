from urllib import request
from django.shortcuts import render
from .forms import PdfGeneratorForm
import fitz
from pathlib import Path
from django.http import FileResponse


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def add_image(pdf, instance):
    # Define which image should be inserted
    img = open(instance.image.path, "rb").read()

    rect = fitz.Rect(450,20,550,120)

    page = pdf[0]
    if not page.is_wrapped:
        page.wrap_contents()
    page.insert_image(rect, stream=img)


def home_page(request):
    context ={}

    if request.method == 'POST':
        form = PdfGeneratorForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save()

            # retrieve the first page of the PDF
            pdf = open(instance.pdf.path)

            doc = fitz.open(pdf, filetype="pdf")

            #call function to add image
            add_image(doc, instance,)
            file_name = "{}{}.pdf".format('new_pdf',instance.id)
            doc.save(file_name)

            result_pdf_path = "{}/{}".format(str(BASE_DIR), file_name)
            # result_pdf = open(result_pdf_path, 'wb')
            # from django.core.files import File

            # with open(result_pdf_path) as f:
                # instance.new_pdf.save(file_name, File(f))
            return FileResponse(open(result_pdf_path, 'rb'), content_type='application/pdf')
    else:
        form = PdfGeneratorForm()
        context['form']= form
        return render(request, "pdfGenerator/home.html", context)
