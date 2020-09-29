from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Test

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BloodtestsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status


class TestDetails(APIView):
    '''
    Get a certain bloodtest or post new bloodtests
    '''
    def get_object_by_name(self, code):
        try:
            return Test.objects.get(code=code)
        except Test.DoesNotExist:
            raise Http404

    def get(self, request, code, format=None):
        bloodtest = self.get_object_by_name(code)
        serializer = BloodtestsSerializer(bloodtest, many=False)
        return Response(serializer.data)

    def head(self, request, code, format=None):
        bloodtest = self.get_object_by_name(code)
        serializer = BloodtestsSerializer(bloodtest, many=False)
        return Response(serializer.data)
    
    def post(self, request, code, format=None):
        #if (request.data['lower'] > request.data['upper']) or ((request.data['lower'] == None) and (request.data['upper'] == None)):
        #    content = {'Error': "Lower value can't exceed upper value"}
        #    return Response(content, 400)
        serializer = BloodtestsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 200)

        return Response(serializer.errors, 400)
