# Generated by Django 3.2.13 on 2023-11-27 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yusmouser', '0006_alter_monnifytransaction_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='cable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cableplan_id', models.CharField(max_length=200)),
                ('cableplan_name', models.CharField(max_length=200)),
                ('cableplan_amount', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(max_length=200)),
                ('network', models.CharField(max_length=200)),
                ('plan_type', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('validity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='data_coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_coupon_id', models.CharField(max_length=200)),
                ('data_coupon_network_name', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='electricity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disco_id', models.CharField(max_length=200)),
                ('disco_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_id', models.CharField(max_length=200)),
                ('network_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='recharge_card_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recharge_id', models.CharField(max_length=200)),
                ('recharge_network_name', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Airtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airtime_type', models.CharField(choices=[('Share and Sell', 'Share and Sell'), ('VTU', 'VTU')], default='1', max_length=15)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='yusmouser.network')),
            ],
        ),
    ]
