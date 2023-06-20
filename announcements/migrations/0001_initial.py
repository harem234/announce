# Generated by Django 4.2.2 on 2023-06-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(default='', max_length=50, verbose_name='titles')),
                ('description', models.CharField(default='', max_length=50, verbose_name='description')),
                ('view counts', models.PositiveIntegerField(default=0, verbose_name='view_counts')),
            ],
        ),
    ]
