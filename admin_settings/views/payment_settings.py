from rest_framework.generics import RetrieveUpdateAPIView
from admin_settings.models import PaymentSettings
from admin_settings.serializers import PaymentSettingsSerializer
from rest_framework.response import Response

class PaymentSettingsAPIView(RetrieveUpdateAPIView):
    queryset = PaymentSettings.objects.all()
    serializer_class = PaymentSettingsSerializer

    def get_object(self):
        return PaymentSettings.objects.first()
