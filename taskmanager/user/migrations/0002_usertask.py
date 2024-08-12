# Generated by Django 5.1 on 2024-08-08 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_users', to='task.task')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_task', to='user.user')),
            ],
        ),
    ]
