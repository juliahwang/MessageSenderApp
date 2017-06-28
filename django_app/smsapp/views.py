# Create your views here.
import sys

from django.http import HttpResponse
from django.shortcuts import render, redirect
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException
from smsapi.apis import api_key, api_secret
from smsapp.forms import SmsForm


def sms_send(request):
    form = SmsForm(data=request.POST)

    def get_valid_sms_info_and_save():
        get_valid_params = {
            'type': request.POST.get('msg_type'),
            'to': request.POST.get('msg_getter'),
            'from': request.POST.get('msg_sender'),
            'text': request.POST.get('msg_text'),
        }
        form.save()
        return get_valid_params

    if request.method == "POST":
        try:
            params = get_valid_sms_info_and_save()
            cool = Message(api_key, api_secret)
            response = cool.send(params)
            success_count = response['success_count']
            print(success_count)
            error_count = response['error_count']
            print(error_count)
            print('Group ID : {}'.format(response['group_id']))

            if 'error_list' in response:
                print('Error List : {}'.format(response['error_list']))
            context = {
                'form': form,
                'success_count': success_count,
                'error_count': error_count,
            }
            return render(request, 'smsapp/sms_result.html', context)

        except CoolsmsException as e:
            return HttpResponse('Error : {} - {}'.format(e.code, e.msg))
    else:
        form = SmsForm()
    context = {
        'form': form,
    }
    return render(request, 'smsapp/sms_send.html', context)
