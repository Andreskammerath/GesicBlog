# Generated by Django 3.0.8 on 2020-08-05 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200731_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.CharField(default='Introduccion', max_length=200),
            preserve_default=False,
        ),
    ]
