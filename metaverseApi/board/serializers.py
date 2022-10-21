from .models import Board
from rest_framework import serializers

class BoardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Board
        fields = ['id', 'title', 'writer', 'create_date', 'count', 'recommend', 'password', 'contents']
