from django.db import models


# Create your models here.
from smsapi.apis import api_owner_num


class SmsSend(models.Model):
    MSG_TYPE_CHOICES = (
        ('sms', 'sms'),
    )
    msg_type = models.CharField(max_length=3, choices=MSG_TYPE_CHOICES, default='sms')
    # IntegerField로 하면 휴대폰 전화번호 첫자리 '0' 이 사라진다.
    msg_getter = models.CharField(max_length=20, blank=False)
    msg_sender = models.CharField(max_length=20, blank=False, default=api_owner_num)
    msg_text = models.TextField(blank=False)

