# Generated by Django 4.1 on 2022-10-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0016_rename_company_id_registrant_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
