import requests
from django.conf import settings

class OTPSender:
    @staticmethod
    def send_otp(phone_number, otp):
        api_url = "http://bulksmsbd.net/api/smsapi"

        message = f"Your OTP is {otp}"

        params = {
            "api_key": settings.BULKSMS_API_KEY,
            "senderid": settings.BULKSMS_SENDER_ID,
            "number": phone_number,
            "message": message
        }

        response = requests.post(api_url, data=params)
        return response