# Generated by Django 3.0.3 on 2020-02-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200206_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='about_us_tagline',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='About us tagline'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='about_us_text',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='About us text'),
        ),
    ]
