from django.urls import path
from .views import GoogleCallback, GoogleAuthorizationURL, test_API

urlpatterns = [
    path("callback/", GoogleCallback.as_view(), name="google_callback"),
    path("google-auth/", GoogleAuthorizationURL.as_view(), name="google_auth"),
    path("test/", test_API.as_view(), name="test_api"),
]