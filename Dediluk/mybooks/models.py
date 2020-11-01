from django.db import models


class Author(models.Model):
    name = models.CharField('Имя', max_length=150)
    image = models.ImageField('Изображение', upload_to='author/')

    def __str__(self):
        return self.name

    def Meta(self):
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    class Meta:
        ordering = ['name']


class Book(models.Model):
    title = models.CharField('Название', max_length=150, blank=False)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='book/')
    author_name = models.ManyToManyField(Author, verbose_name='Авторы', related_name="books_author")

    def __str__(self):
        return self.title

    def Meta(self):
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    class Meta:
        ordering = ['title']
