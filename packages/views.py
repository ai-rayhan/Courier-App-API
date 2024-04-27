from .models import Parcel,Issue,ParcelDetails,ReturnParcel
from .serializers import ParcelSerializer,IssueSerializer,ParcelDetailsSerializer,ReturnParcelSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ParcelList(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]
class ParcelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]

class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]
class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

class ParcelDetailsList(generics.ListCreateAPIView):
    queryset = ParcelDetails.objects.all()
    serializer_class = ParcelDetailsSerializer
    permission_classes = [IsAuthenticated]
class ParcelDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParcelDetails.objects.all()
    serializer_class = ParcelDetailsSerializer
    permission_classes = [IsAuthenticated]

class ReturnParcelList(generics.ListCreateAPIView):
    queryset = ReturnParcel.objects.all()
    serializer_class = ReturnParcelSerializer
    permission_classes = [IsAuthenticated]
class ReturnParcelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReturnParcel.objects.all()
    serializer_class = ReturnParcelSerializer
    permission_classes = [IsAuthenticated]
