from django.db import models
from django.shortcuts import reverse


class Task(models.Model):
    task_title = models.CharField(max_length=100)
    due_date = models.DateField()
    description = models.TextField(max_length=250)

    def get_detail_url(self):
        return reverse('tasks:task_detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('tasks:task_delete', args=[self.pk])

    def get_update_url(self):
        return reverse('tasks:task_update', args=[self.pk])
