from django.forms import ModelForm
from .models import PdfGenerator


class PdfGeneratorForm(ModelForm):

     class Meta:
        model = PdfGenerator
        fields = ['image', 'pdf']
