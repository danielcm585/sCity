# Generated by Django 4.1 on 2022-10-12 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0004_alter_project_chosen_registrant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='chosen_registrant',
            new_name='chosen_registrant_id',
        ),
    ]
