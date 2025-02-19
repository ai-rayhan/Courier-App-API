from rest_framework.response import Response
from rest_framework import status

def custom_response(data=None, error="", status=status.HTTP_200_OK, success=True):
    if not success:
        return Response({
            'status': success,
            'error': error,
        }, status=status)
    else:
        return Response({
            'status': success,
            'data': data,
        }, status=status)
