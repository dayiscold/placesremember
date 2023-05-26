# Generated by Django 4.2.1 on 2023-05-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tablish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Воспоминание', max_length=50, verbose_name='Название места')),
                ('memory_text', models.TextField(verbose_name='Напишите Отзыв')),
                ('date_memory_publish', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]