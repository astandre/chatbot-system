from rest_framework import serializers


class QuestionSerializer(serializers.Serializer):
    query = serializers.CharField(required=True, max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return validated_data
