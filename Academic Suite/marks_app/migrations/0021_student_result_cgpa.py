# Generated by Django 4.1.5 on 2024-01-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks_app', '0020_student_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_result',
            name='cgpa',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
