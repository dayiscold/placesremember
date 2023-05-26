from django.db import models


class Tablish(models.Model):
    title = models.CharField('Название места', max_length=50, default='Воспоминание')
    memory_text = models.TextField('Напишите Отзыв')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = 'Воспоминания'

