from django.urls import path
from .views import GithubCallback, GithubLogin, test_API

urlpatterns = [
    path("callback/", GithubCallback.as_view(), name="github_callback"),
    path("auth/", GithubLogin.as_view(), name="github_auth"),
    path("test/", test_API.as_view(), name="github_test"),
]