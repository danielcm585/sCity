# Generated by Django 4.1 on 2022-10-12 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('closed_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='registrant',
            name='tender_id',
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='company_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tender.company'),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Tender',
        ),
        migrations.AddField(
            model_name='project',
            name='chosen_registrant',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.registrant'),
        ),
        migrations.AddField(
            model_name='registrant',
            name='project_id',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='tender.project'),
            preserve_default=False,
        ),
    ]
