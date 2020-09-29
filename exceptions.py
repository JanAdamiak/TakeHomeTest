from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError



def custom_drf_exception_handler(exc, context):
    print (exc, context)
    response = exception_handler(exc, context)
    if response:
        return response
    else:
        return Response({'Error': 'Data cannot be parsed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
