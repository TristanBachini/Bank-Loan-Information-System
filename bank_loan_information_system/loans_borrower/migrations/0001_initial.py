# Generated by Django 4.0.3 on 2022-05-26 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('app_no', models.IntegerField(blank=True, null=True)),
                ('brand', models.CharField(max_length=100, null=True)),
                ('loan_amt', models.IntegerField(blank=True, null=True)),
                ('int_rate', models.CharField(max_length=50, null=True)),
                ('no_of_payments', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('For Review', 'For Review'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=100, null=True)),
                ('principal', models.IntegerField(blank=True, null=True)),
                ('rem_bal', models.IntegerField(blank=True, null=True)),
                ('next_due', models.DateField(null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
