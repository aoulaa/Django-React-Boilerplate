from dj_rest_auth.views import UserDetailsView
from django.urls import path

urlpatterns = [
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
]
