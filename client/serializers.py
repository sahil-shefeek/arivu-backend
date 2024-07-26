from rest_framework import serializers
from client.models import GPTQuery


class GPTQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GPTQuery
        fields = '__all__'
