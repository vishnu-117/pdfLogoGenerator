# Generated by Django 4.1.1 on 2022-09-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfGenerator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfgenerator',
            name='new_pdf',
            field=models.FileField(blank=True, null=True, upload_to='new-pdf/'),
        ),
    ]
