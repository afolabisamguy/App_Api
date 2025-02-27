from rest_framework import serializers

from api.post.querysets import PUBLIC_POSTS_QUERYSET
from content.models import Comment
from api.user.serializers import UserPublicSerializer


class CommentSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "uuid",
            "owner",
            "body",
            "created_at",
        ]

        read_only_fields = [
            "uuid",
            "owner",
            "created_at",
        ]


class CommentCreateSerializer(serializers.Serializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    post = serializers.SlugRelatedField(
        slug_field="uuid",
        queryset=PUBLIC_POSTS_QUERYSET,
    )

    body = serializers.CharField()
