from django.shortcuts import render

# Create your views here.
import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

if __name__ == '__main__':
    api_key = 'NCSGLMHSQ2FTVZUA'
    api_secret = '2ZNM5ZPZR07QHSLHVIFAH3XZR1GAGM2F'

    params = dict()
    params['type'] = 'sms'
    params['to'] = '01048152941'
    params['from'] = '01029953874'
    params['text'] = '보내져라 얍얍'

    cool = Message(api_key, api_secret)
    try:
        response = cool.send(params)
        print('Success Count : {}'.format(response['success_count']))
        print('Error Count : {}'.format(response['error_count']))
        print('Group ID : {}'.format(response['group_id']))

        if 'error_list' in response:
            print('Error List : {}'.format(response['error_list']))

    except CoolsmsException as e:
        print('Error Code : {}'.format(e.code))
        print('Error Message : {}'.format(e.msg))

    sys.exit()
