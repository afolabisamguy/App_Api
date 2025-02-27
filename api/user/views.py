from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)


from api.permissions import AllowAny, IsAuthenticated
from api.user.querysets import ALL_USERS_QUERYSET
from api.user.serializers import UserMeSerializer, UserPublicSerializer


class UserApiView(GenericAPIView):
    serializer_class = UserPublicSerializer
    queryset = ALL_USERS_QUERYSET
    permission_classes = [AllowAny]

    search_fields = ["name"]
    ordering_fields = ["created_at"]
    ordering = "-created_at"


class UserMeApiView(UserApiView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserMeSerializer

    def get_object(self):
        return self.request.user


class UserListView(ListModelMixin, UserApiView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserRetrieveView(RetrieveModelMixin, UserApiView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UserMeRetrieveUpdateView(RetrieveModelMixin, UpdateModelMixin, UserMeApiView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
