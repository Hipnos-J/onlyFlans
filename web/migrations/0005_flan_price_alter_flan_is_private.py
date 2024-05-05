# Generated by Django 4.2 on 2024-05-05 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_flan_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='price',
            field=models.DecimalField(decimal_places=0, default=1000, max_digits=4),
        ),
        migrations.AlterField(
            model_name='flan',
            name='is_private',
            field=models.BooleanField(),
        ),
    ]