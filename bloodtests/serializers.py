from rest_framework import serializers
from .models import Test

class BloodtestsSerializer(serializers.ModelSerializer):


    ideal_range = serializers.ReadOnlyField(source='combined')

    class Meta:
        model = Test
        fields = ['ideal_range', 'code', 'name', 'unit', 'lower', 'upper']
