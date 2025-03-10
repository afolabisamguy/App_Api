from django.urls import path


urlpatterns = [
    path("", UserListView.as_view()),
    path("me/", UserMeRetrieveUpdateView.as_view()),
    path("<uuid:uuid>/", UserRetrieveView.as_view(lookup_field="uuid")),
    path("<int:pk>/", UserRetrieveView.as_view()),
]
