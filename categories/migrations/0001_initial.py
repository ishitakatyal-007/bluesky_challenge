# Generated by Django 3.2.5 on 2021-11-15 06:30

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmissionCategories',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('category_id', models.AutoField(help_text='Emission category', primary_key=True, serialize=False, verbose_name='Emission Category')),
                ('category_description', models.TextField(help_text='Category description', verbose_name='Category Decription')),
                ('category_alias', models.CharField(help_text='Alias for category', max_length=10, unique=True, verbose_name='Category Alias')),
            ],
            options={
                'verbose_name': 'Emission Categorie',
                'db_table': 'emission_categories',
                'ordering': ('created',),
            },
        ),
    ]
