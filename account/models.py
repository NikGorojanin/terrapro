from enum import Enum

from django.db import models

from terrapro_admin.models import BaseModel


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'

    @classmethod
    def choices(cls):
        return list((i.name, i.value) for i in cls)


class Language(Enum):
    RUS = 'rus'
    UZB = 'uzb'
    ENG = 'eng'

    @classmethod
    def choices(cls):
        return list((i.name, i.value) for i in cls)


class User(BaseModel):
    telegram_id = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=100, null=True, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100, null=True, blank=True)
    fio = models.CharField(verbose_name='ФИО', max_length=100, null=True, blank=True)
    telegram_username = models.CharField(verbose_name='Телеграм', max_length=100, null=True, blank=True)
    gender = models.CharField(verbose_name='Пол', choices=Gender.choices(), max_length=10, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    registration_time = models.DateTimeField(null=True, blank=True)
    language = models.CharField(verbose_name='Язык', choices=Language.choices(), max_length=10, null=True, blank=True)
    is_admin = models.IntegerField(default=0)
    phone = models.CharField(verbose_name='Телефон', max_length=100, null=True, blank=True)
    id_1c = models.CharField(verbose_name='1C ID', max_length=100, null=True, blank=True)

    @classmethod
    def get_or_create(cls, id_1c, phone):
        user = cls.objects.filter(id_1c=id_1c).first()

        if not user:
            user = User(id_1c=id_1c, phone=phone)
            user.save()

        return user

    class Meta:
        db_table = 'users'

    def __str__(self):
        return '{} {}'.format(self.first_name or '', self.last_name or '')
