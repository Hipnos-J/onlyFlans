# Generated by Django 4.2 on 2024-04-18 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
