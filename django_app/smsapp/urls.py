from django.conf.urls import url

from smsapp import views

app_name = 'smsapp'

urlpatterns = [
    url(r'^send/$', views.sms_send, name='sms_send'),
]
