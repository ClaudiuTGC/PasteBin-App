# Generated by Django 3.1.7 on 2021-03-16 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bins', '0036_auto_20210315_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binss',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Binss', to=settings.AUTH_USER_MODEL),
        ),
    ]
