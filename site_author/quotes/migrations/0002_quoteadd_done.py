# Generated by Django 5.0.4 on 2024-05-01 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoteadd',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
