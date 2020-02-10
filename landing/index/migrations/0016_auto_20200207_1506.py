# Generated by Django 3.0.3 on 2020-02-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_indexpage_telegram'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone number')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram')),
                ('telegram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telegram')),
                ('short_about', models.CharField(blank=True, max_length=300, null=True, verbose_name='Short about')),
            ],
            options={
                'verbose_name': 'Site settings',
            },
        ),
        migrations.RemoveField(
            model_name='indexpage',
            name='email',
        ),
        migrations.RemoveField(
            model_name='indexpage',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='indexpage',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='indexpage',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='indexpage',
            name='short_about',
        ),
        migrations.RemoveField(
            model_name='indexpage',
            name='telegram',
        ),
    ]