from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from utils.github_utils import get_access_token_from_github, get_user_info_from_github
from google_api.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK


# Create your views here.
class GithubCallback(APIView):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return Response({"error": "Authorization code missing"}, status=400)
        return Response({"code": code})
    

class GithubLogin(APIView):
    def get(self, request):
        client_id = settings.SOCIAL_AUTH_GITHUB_CLIENT_ID
        redirect_uri = settings.SOCIAL_AUTH_GITHUB_REDIRECT_URI
        state = settings.SOCIAL_AUTH_GITHUB_STATE
        auth_url = f"https://github.com/login/oauth/authorize?client_id={client_id}&response_type=code&scope=repo&redirect_uri={redirect_uri}&state={state}"
        return Response({"auth_url": auth_url})
    
    def post(self, request):
        """Handles GitHub OAuth authentication and user login."""
        code = request.data.get('auth_code')
        if not code:
            return Response({"error": "Authorization code missing"}, status=HTTP_400_BAD_REQUEST)

        access_token_data = get_access_token_from_github(code)
        if "error" in access_token_data:
            return Response({"error": access_token_data["error"]}, status=HTTP_400_BAD_REQUEST)

        user_info = get_user_info_from_github(access_token_data.get('access_token'))
        if "error" in user_info:
            return Response({"error": user_info["error"]}, status=HTTP_400_BAD_REQUEST)

        username = f"{user_info.get('login')}_{user_info.get('id')}"
        name = user_info.get("name", "")
        email = f"{username}@yopmail.com"

        user, _ = User.objects.get_or_create(
            username=username,
            defaults={"email": email, "is_verified": True, "name": name, "auth_provider": "github"}
        )

        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)

        return Response({
            "message": "Login successful",
            "user": {"username": username, "name": name},
            "token": token.key
        }, status=HTTP_200_OK)
    

class test_API(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        return Response({"message": "Hello, world!"})
