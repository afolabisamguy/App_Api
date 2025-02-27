from rest_framework import serializers
from api.user.serializers import UserPublicSerializer
from content.models import Post


class PostSerializer(serializers.ModelSerializer):

    owner = UserPublicSerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "uuid",
            "title",
            "body",
            "status",
            "created_at",
            "owner",
        ]

        read_only_fields = [
            "id",
            "uuid",
            "owner",
            "created_at",
            "owner",
        ]
