# Generated by Django 3.2 on 2021-05-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0008_auto_20210530_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
