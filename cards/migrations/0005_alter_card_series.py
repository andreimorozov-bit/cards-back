# Generated by Django 3.2.9 on 2021-11-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20211119_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='series',
            field=models.CharField(max_length=7),
        ),
    ]
