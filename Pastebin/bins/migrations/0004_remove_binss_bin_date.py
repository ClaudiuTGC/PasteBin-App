# Generated by Django 3.1.7 on 2021-03-11 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bins', '0003_auto_20210308_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='binss',
            name='bin_date',
        ),
    ]
