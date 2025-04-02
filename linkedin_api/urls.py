from django.urls import path
from .views import LinkedinCallback, LinkedinLogin, test_API

urlpatterns = [
    path("callback/", LinkedinCallback.as_view(), name="linkedin_callback"),
    path("auth/", LinkedinLogin.as_view(), name="linkedin_auth"),
    path("test/", test_API.as_view(), name="github_test"),
]