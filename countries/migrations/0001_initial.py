# Generated by Django 3.2.5 on 2021-11-15 06:30

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('country_id', models.AutoField(help_text='Unique ID for country', primary_key=True, serialize=False, verbose_name='Country Unique ID')),
                ('country_name', models.CharField(help_text='Country name', max_length=100, verbose_name='Name of the country')),
            ],
            options={
                'verbose_name': 'Countrie',
                'db_table': 'countries',
                'ordering': ('country_name',),
            },
        ),
    ]
