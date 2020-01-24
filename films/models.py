from django.db import models as mds
from django.db.models import Q
from easy_thumbnails.fields import ThumbnailerImageField

from settings.global_params import *
from settings.paths import VIDEO_PATH


# Create your models here.
class Genre(mds.Model):
    name = mds.CharField(max_length=MIDDLE_CHARS, blank=True, primary_key=True, verbose_name='название жанра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Actor(mds.Model):
    first_name = mds.CharField(max_length=SHORT_CHARS, blank=True, default='Actor', verbose_name='имя актера')
    second_name = mds.CharField(max_length=SHORT_CHARS, blank=True, default='Actor', verbose_name='фамилия актера')
    citizen = mds.CharField(max_length=SHORT_CHARS, default='Author', verbose_name='гражданство актера')

    def __str__(self):
        return self.first_name+" "+self.second_name

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Director(mds.Model):
    first_name = mds.CharField(max_length=SHORT_CHARS, blank=True, default='Author', verbose_name='имя')
    second_name = mds.CharField(max_length=SHORT_CHARS, blank=True, default='Author', verbose_name='фамилия')
    citizen = mds.CharField(max_length=SHORT_CHARS, default='Author', verbose_name='гражданство')

    def __str__(self):
        return self.first_name+" "+self.second_name

    class Meta:
        verbose_name = 'Режисер'
        verbose_name_plural = 'Режисеры'


class Film(mds.Model):
    title = mds.CharField(max_length=SHORT_CHARS, blank=True, default='', verbose_name='название')
    year = mds.IntegerField(blank=True, default=2020, verbose_name='год создания')
    city = mds.CharField(max_length=SHORT_CHARS, verbose_name='страна-создатель')
    photo = ThumbnailerImageField(upload_to='photos', blank=True, verbose_name='фото фасада')
    info = mds.TextField(verbose_name='краткая информация о сюжете', default='')
    quality = mds.CharField(max_length=SHORT_CHARS, verbose_name='качество видео', default='480p')
    duration = mds.IntegerField(blank=True, default=60, verbose_name='продолжительность фильма')
    rating = mds.IntegerField(verbose_name='колличество звезд', null=True)
    video = mds.FileField(upload_to='videos', verbose_name='видео файл')
    min_age = mds.IntegerField(verbose_name='минимальный возраст', blank=True,  default=18)

    genres = mds.ManyToManyField(Genre)
    directors = mds.ManyToManyField(Director)
    actors = mds.ManyToManyField(Actor)

    def __str__(self):
        return self.title+" "+str(self.year)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

        indexes = [
            mds.Index(fields=['title'], name='film_name_idx')
        ]



