# Generated by Django 4.1 on 2022-10-19 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0015_alter_registrant_deal_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrant',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='registrant',
            old_name='project_id',
            new_name='project',
        ),
        migrations.AlterField(
            model_name='registrant',
            name='offer_price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('registrant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tender.registrant')),
            ],
        ),
    ]