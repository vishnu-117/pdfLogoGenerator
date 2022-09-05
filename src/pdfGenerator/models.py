from django.db import models

class PdfGenerator(models.Model):
    image = models.ImageField(upload_to = "images/", null=True, blank=True)
    pdf = models.FileField(upload_to = "pdf/", null=True, blank=True)
    new_pdf = models.FileField(upload_to = "new-pdf/", null=True, blank=True)

