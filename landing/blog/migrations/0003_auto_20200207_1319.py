# Generated by Django 3.0.3 on 2020-02-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200207_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('created',), 'verbose_name': 'Post'},
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=500, verbose_name='Name'),
            preserve_default=False,
        ),
    ]