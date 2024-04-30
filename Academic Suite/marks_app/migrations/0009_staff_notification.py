# Generated by Django 5.0 on 2024-01-19 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks_app', '0008_alter_student_session_year_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marks_app.staff')),
            ],
        ),
    ]
