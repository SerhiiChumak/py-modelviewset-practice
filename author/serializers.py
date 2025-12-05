from rest_framework import serializers
from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    pseudonym = serializers.CharField(
        max_length=64,
        required=False,
        allow_null=True
    )
    age = serializers.IntegerField()
    retired = serializers.BooleanField()

    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "last_name",
            "pseudonym",
            "age",
            "retired"
        )

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
