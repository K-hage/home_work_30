from rest_framework import serializers

from ads.models import Selection
from ads.serializers import AdSerializer


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['id', 'name']


class SelectionSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        validated_data['owner'] = instance.owner
        return super().update(instance, validated_data)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'
