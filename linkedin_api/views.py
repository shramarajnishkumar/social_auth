from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from utils.linkedin_utils import get_access_token_from_linkedin, get_user_info_from_linkedin
from google_api.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
import urllib.parse


# Create your views here.
class LinkedinCallback(APIView):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return Response({"error": "Authorization code missing"}, status=400)
        return Response({"code": code})
    

class LinkedinLogin(APIView):
    def get(self, request):
        LINKEDIN_AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
        params = {
            "response_type": "code",
            "client_id": settings.SOCIAL_AUTH_LINKEDIN_CLIENT_ID,
            "redirect_uri": settings.SOCIAL_AUTH_LINKEDIN_REDIRECT_URI,
            "scope": "openid profile email w_member_social",
            "state": "asdgkhasalid"
        }
        auth_url = f"{LINKEDIN_AUTH_URL}?{urllib.parse.urlencode(params)}"
        return Response({"auth_url": auth_url})
    
    def post(self, request):
        """Handles LINKEDIN OAuth authentication and user login."""
        code = request.data.get('auth_code')
        if not code:
            return Response({"error": "Authorization code missing"}, status=HTTP_400_BAD_REQUEST)

        access_token_data = get_access_token_from_linkedin(code)
        if "error" in access_token_data:
            return Response({"error": access_token_data["error"]}, status=HTTP_400_BAD_REQUEST)

        user_info = get_user_info_from_linkedin(access_token_data.get('access_token'))
        if "error" in user_info:
            return Response({"error": user_info["error"]}, status=HTTP_400_BAD_REQUEST)

        name = user_info.get("name", "")
        email = user_info.get('email')

        user, _ = User.objects.get_or_create(
            username=email,
            defaults={"email": email, "is_verified": True, "name": name, "auth_provider": "linkedin"}
        )

        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)

        return Response({
            "message": "Login successful",
            "user": {"email": email, "name": name},
            "token": token.key
        }, status=HTTP_200_OK)
    
class test_API(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        return Response({"message": "Hello, world!"})  # pragma: no cover