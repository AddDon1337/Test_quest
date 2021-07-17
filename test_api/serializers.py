from rest_framework import serializers
from test_api.models import Deal


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ['customer', 'item', 'total', 'quantity', 'date']

    def create(self, validated_data):
        """
        Create and return a new `Deal` instance, given the validated data.
        """
        return Deal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Deal` instance, given the validated data.
        """
        instance.customer = validated_data.get('customer', instance.customer)
        instance.item = validated_data.get('item', instance.item)
        instance.total = validated_data.get('total', instance.total)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

