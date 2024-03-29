# Generated by Django 3.2.13 on 2023-07-06 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yusmouser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='DataTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=200)),
                ('ident', models.CharField(max_length=200)),
                ('balance_before', models.CharField(max_length=200)),
                ('balance_after', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('plan_network', models.CharField(max_length=200)),
                ('plan_name', models.CharField(max_length=200)),
                ('plan_amount', models.CharField(max_length=200)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('ported_number', models.CharField(max_length=200)),
                ('api_response', models.CharField(max_length=2000)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AirtimeTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=200)),
                ('ident', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('plan_network', models.CharField(max_length=200)),
                ('airtime_type', models.CharField(max_length=200)),
                ('paid_amount', models.CharField(max_length=200)),
                ('balance_before', models.CharField(max_length=200)),
                ('balance_after', models.CharField(max_length=200)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('ported_number', models.CharField(max_length=200)),
                ('api_response', models.CharField(max_length=2000)),
                ('customer_ref', models.CharField(max_length=2000)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
