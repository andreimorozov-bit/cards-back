# Generated by Django 3.2.9 on 2021-11-26 16:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_alter_card_series'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardCollection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('series', models.CharField(max_length=6)),
                ('expiration_months', models.IntegerField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
