# Generated by Django 3.0.3 on 2020-02-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20200207_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='first_type_description',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='First type description'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='first_type_header',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='First type name'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='second_type_description',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Second type name'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='second_type_header',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Second type name'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='types_header',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Types header'),
        ),
    ]