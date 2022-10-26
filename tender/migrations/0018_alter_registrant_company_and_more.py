# Generated by Django 4.1 on 2022-10-25 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0017_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrant',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='tender.company'),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='offer_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrants', to='tender.project'),
        ),
    ]
