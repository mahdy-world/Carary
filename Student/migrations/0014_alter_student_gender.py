# Generated by Django 3.2 on 2021-05-18 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0013_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Gender',
            field=models.CharField(choices=[('انثي', 'انثي'), ('ذكر', 'ذكر')], max_length=40, verbose_name='النوع'),
        ),
    ]
