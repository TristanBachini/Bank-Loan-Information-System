# Generated by Django 4.0.4 on 2022-06-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans_borrower', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='loan_docs',
            field=models.FileField(blank=True, null=True, upload_to='loan_doc/'),
        ),
    ]
