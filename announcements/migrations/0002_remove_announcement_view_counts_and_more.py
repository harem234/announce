# Generated by Django 4.2.2 on 2023-06-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='view counts',
        ),
        migrations.AddField(
            model_name='announcement',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='view_counts'),
        ),
    ]
