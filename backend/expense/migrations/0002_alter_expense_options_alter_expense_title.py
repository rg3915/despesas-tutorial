# Generated by Django 4.2.6 on 2023-10-24 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('title',), 'verbose_name': 'Despesa', 'verbose_name_plural': 'Despesas'},
        ),
        migrations.AlterField(
            model_name='expense',
            name='title',
            field=models.CharField(max_length=5, verbose_name='título'),
        ),
    ]