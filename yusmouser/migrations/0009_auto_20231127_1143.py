# Generated by Django 3.2.13 on 2023-11-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yusmouser', '0008_auto_20231127_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cable',
            old_name='cableplan_id',
            new_name='cable_id',
        ),
        migrations.AddField(
            model_name='cableplan',
            name='cableplan_id',
            field=models.CharField(default=4, max_length=200),
            preserve_default=False,
        ),
    ]
