# Generated by Django 3.1.7 on 2021-03-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bins', '0002_auto_20210308_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Binss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('bin_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Bins',
        ),
    ]
