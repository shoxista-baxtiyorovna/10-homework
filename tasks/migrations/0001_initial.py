# Generated by Django 4.2.17 on 2024-12-14 05:40

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
                ('task_title', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]
