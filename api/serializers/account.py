from rest_framework import serializers


class AccountSerializer(serializers.Serializer):
    data = serializers.ListField()

    def validate(self, validated_data):
        return validated_data['data']
