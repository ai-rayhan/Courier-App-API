
from abc import ABC, abstractmethod
from django.conf import settings
import random
import requests
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

from admin_settings.models import SmsProvider

# Abstract base class for SMS providers
class BaseSMSProvider(ABC):
    
    @abstractmethod
    def send_sms(self, to, message):
        pass

# Twilio SMS Provider Implementation
class TwilioSMSProvider(BaseSMSProvider):
    
    def __init__(self, account_sid, auth_token, from_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send_sms(self, to, message):
        try:
            message = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to
            )
            return {
                'status': message.status,
                'sid': message.sid
            }
        except TwilioRestException as e:
            return {
                'status': 'failed',
                'error': str(e)
            }

# BulkSMS Provider Implementation
class BulkSMSSMSProvider(BaseSMSProvider):
    
    def __init__(self, api_key, sender_id):
        self.api_key = api_key
        self.sender_id = sender_id

    def send_sms(self, to, message):
        api_url = "http://bulksmsbd.net/api/smsapi"
        params = {
            "api_key": self.api_key,
            "senderid": self.sender_id,
            "number": to,
            "message": message
        }
        response = requests.post(api_url, data=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {
                'status': 'failed',
                'error': response.text
            }
        
def get_sms_provider_credentials():
    try:
        provider = SmsProvider.objects.get(status=True)
        return {
            'account_sid': provider.account_sid,
            'auth_token': provider.auth_token,
            'from_number': provider.from_number,
            'api_key': provider.api_key,
            'sender_id': provider.sender_id
        }
    except SmsProvider.DoesNotExist:
        return None