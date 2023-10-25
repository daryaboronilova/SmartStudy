from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    short_dest = models.CharField(max_length=255, verbose_name='Краткое описание новостей')
    content = models.TextField(verbose_name='Контент')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    photo = models.ImageField(upload_to='images/', verbose_name='Фото', blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
