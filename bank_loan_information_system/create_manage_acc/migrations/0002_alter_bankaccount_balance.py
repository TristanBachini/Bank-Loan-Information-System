# Generated by Django 4.0.4 on 2022-06-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_manage_acc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
    ]
