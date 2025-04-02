from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
import google.oauth2.credentials
import google_auth_oauthlib.flow
import requests
from .models import User
from utils.google_utils import get_google_user_info


class GoogleCallback(APIView):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return Response({"error": "Authorization code missing"}, status=400)
        return Response({"code": code})


class GoogleAuthorizationURL(APIView):
    def get(self, request):
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            'client_secret_985658929471-56p1mkao4hkeqn40q5psepr0mdia8o49.apps.googleusercontent.com.json',
            scopes=[
                'https://www.googleapis.com/auth/userinfo.email',
                'https://www.googleapis.com/auth/userinfo.profile',
                'openid'
                ]
            )
        flow.redirect_uri = 'http://127.0.0.1:8000/google/callback/'

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
            login_hint='hint@example.com',
            prompt='consent'
            )
        return Response({'url': authorization_url})
    
    def post(self, request):
        data = request.data.copy()
        auth_code = data.get("code")
        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "code": auth_code,
            "client_id": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
            "client_secret": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
            "redirect_uri": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI,
            "grant_type": "authorization_code"
        }
        response = requests.post(token_url, data=data)
        access_token = response.json().get("access_token")
        user_info = get_google_user_info(access_token)
        email = user_info.get("email")
        name = user_info.get("name")
        user, created = User.objects.get_or_create(username=email, email=email,is_verified=True, name=name, auth_provider="google")
        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            "message": "Login successful",
            "user": {"email": email, "name": name},
            "token": token.key
        })


class test_API(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        return Response({"message": "Hello, world!"})  # pragma: no cover
    



