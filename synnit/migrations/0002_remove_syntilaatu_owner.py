# Generated by Django 2.2.4 on 2019-08-13 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('synnit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syntilaatu',
            name='owner',
        ),
    ]