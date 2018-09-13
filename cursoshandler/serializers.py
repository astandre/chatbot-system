from rest_framework import serializers


class CursoSerializer(serializers.Serializer):
    curso = serializers.CharField(required=False, max_length=50)
    codigo = serializers.CharField(required=False, max_length=50)
    synonym = serializers.CharField(required=False, max_length=20)

    def create(self, validated_data):
        return validated_data
