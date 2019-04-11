from rest_framework import serializers

from .models import Garments


class GarmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garments
        fields = '__all__'