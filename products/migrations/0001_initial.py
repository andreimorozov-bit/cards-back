# Generated by Django 3.2.9 on 2021-11-18 14:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(default='', max_length=500)),
                ('description', models.TextField(default='')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('inventory', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]