# Generated by Django 4.0.4 on 2022-05-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans_borrower', '0003_remove_loans_app_no_remove_loans_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='civ_status',
            field=models.CharField(blank=True, choices=[('Married', 'Married'), ('Separated', 'Separated'), ('Single', 'Single'), ('Widower', 'Widower')], max_length=100, null=True),
        ),
    ]