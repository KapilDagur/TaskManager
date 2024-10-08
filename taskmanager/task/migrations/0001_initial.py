# Generated by Django 5.1 on 2024-08-08 12:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Task ID')),
                ('task_title', models.CharField(max_length=255, verbose_name='Task Title')),
                ('task_description', models.TextField(blank=True, null=True, verbose_name='Task Description')),
                ('task_file', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Attach File(Any)')),
                ('task_url', models.URLField(blank=True, null=True, verbose_name='URL(Any)')),
                ('task_status', models.BooleanField(default=False, verbose_name='Task Status')),
            ],
        ),
    ]
