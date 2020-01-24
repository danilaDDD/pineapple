from django.db import models as mds

from settings.global_params import *
from films.models import Film


# Create your models here.
class User(mds.Model):
    phone = mds.CharField(max_length=LONG_CHARS, blank=True, primary_key=True, verbose_name='телефон', unique=True)
    login = mds.CharField(max_length=LONG_CHARS, blank=True, verbose_name='логин')
    password = mds.CharField(max_length=LONG_CHARS, blank=True, verbose_name='пароль')
    email = mds.EmailField(verbose_name='email', null=True)
    age = mds.IntegerField(blank=True, verbose_name='возраст')

    indexes = [
        mds.Index(fields=['login'], name='login_idx'),
        mds.Index(fields=['password'], name='passwd_idx')
    ]

    class Meta:
        verbose_name = 'Подпосчик'
        verbose_name_plural = 'подписчики'

    def __str__(self):
        return self.login+" "+self.password


class Tarifs(mds.Model):
    name = mds.CharField(max_length=LONG_CHARS, blank=True, primary_key=True, verbose_name='имя')
    info = mds.TextField(verbose_name='полная информация')
    price = mds.IntegerField(verbose_name='цена в месяц', blank=True)
    duration = mds.IntegerField(verbose_name='продолжительность в месяцах', blank=True)

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'тарифы'

    def __str__(self):
        return self.name


class Orders(mds.Model):
    user = mds.ForeignKey(User, on_delete=mds.CASCADE)
    tarif = mds.ForeignKey(Tarifs, on_delete=mds.SET_NULL, null=True)
    date_time = mds.DateTimeField(blank=True, verbose_name='дата совершения')

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'сделки'
        index_together = ['user', 'tarif']

    def __str__(self):
        return self.user.phone+" "+self.tarif.name


class UsedFilms(mds.Model):
    user = mds.ForeignKey(User, on_delete=mds.CASCADE)
    film = mds.ForeignKey(Film, on_delete=mds.CASCADE)
    status = mds.CharField(max_length=SHORT_CHARS, blank=True, verbose_name='текущий статус')
    datetime = mds.DateTimeField(verbose_name='', blank=True)

    class Meta:
        verbose_name = 'Используемый фильм'
        verbose_name_plural = 'используемые фильмы'

    def __str__(self):
        return self.user.phone+" "+self.film.name+" "+self.status




