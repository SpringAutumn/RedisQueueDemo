from rest_framework import serializers
from fresh import models


class FreshSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fresh
        fields = ('id', 'title')
