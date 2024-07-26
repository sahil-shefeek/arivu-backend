from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from client.serializers import GPTQuerySerializer
from client.utils import process_query


class QueryPromptAPIView(APIView):
    def post(self, request):
        serializer = GPTQuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data['query']
            response = process_query(query)
            return Response({'response': response}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
