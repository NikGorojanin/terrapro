from django.db import models

from terrapro_admin.models import BaseModel
from account.models import User


class Post(BaseModel):
    is_published = models.BooleanField(default=False)
    text = models.CharField(max_length=2000, null=True, blank=True)
    tg_image_id = models.CharField(max_length=200, null=True, blank=True)
    tg_video_id = models.CharField(max_length=200, null=True, blank=True)
    tg_document_id = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'posts'


class FeedbackMessage(BaseModel):
    telegram_id = models.IntegerField()
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    telegram_username = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=2000, null=True, blank=True)
    tg_voice_id = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'feedback_messages'


class Cite(BaseModel):
    en_name = models.CharField(max_length=100)
    ru_name = models.CharField(max_length=100, null=True, blank=True)
    uz_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'cites'


class Branche(BaseModel):
    address = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name='branches', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'branches'


class Account(BaseModel):
    user = models.ForeignKey(User, related_name='accounts', on_delete=models.DO_NOTHING, null=True, blank=True)
    barcode = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100)
    total_balance = models.FloatField(default=0.0)
    total_spent_monthly = models.FloatField(default=0.0)
    total_spent_yearly = models.FloatField(default=0.0)
    total_spent = models.FloatField(default=0.0)
    birthday = models.DateField(null=True, blank=True)
    id_1c = models.CharField(verbose_name='1C ID', max_length=100, unique=True, db_index=True)

    class Meta:
        db_table = 'accounts'