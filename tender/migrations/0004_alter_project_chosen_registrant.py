# Generated by Django 4.1 on 2022-10-12 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0003_alter_registrant_company_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='chosen_registrant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.registrant'),
        ),
    ]
