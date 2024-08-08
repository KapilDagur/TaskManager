from django.db import models
import uuid

class Task(models.Model):

    #Task Id
    task_id = models.UUIDField(
        verbose_name='Task ID',
        name='task_id',
        primary_key=False,
        default=uuid.uuid4,
        editable=False
    )

    #Task Title
    task_title = models.CharField(
        verbose_name='Task Title',
        name='task_title',
        max_length=255,
        null=False,
        blank=False
    )

    #Task Description
    task_description = models.TextField(
        verbose_name='Task Description',
        name='task_description',
        null=True,
        blank=True
    )

    #Attach File Field
    attach_file = models.FileField(
        verbose_name='Attach File(Any)',
        name='task_file',
        upload_to='uploads/',
        null=True,
        blank=True
    )

    #Hyperlink Field
    url = models.URLField(
        verbose_name='URL(Any)',
        name='task_url',
        max_length=200,
        null=True,
        blank=True
    )

    #Status Field
    status = models.BooleanField(
        verbose_name='Task Status',
        name='task_status',
        default=False
    )

    def __str__(self):
        return self.task_title
