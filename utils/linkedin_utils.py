import requests
from django.conf import settings

def get_access_token_from_linkedin(auth_code):
    """Exchange authorization code for GitHub access token."""
    try:
        response = requests.post(
            settings.SOCIAL_AUTH_LINKEDIN_ACCESS_TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "client_id": settings.SOCIAL_AUTH_LINKEDIN_CLIENT_ID,
                "client_secret": settings.SOCIAL_AUTH_LINKEDIN_CLIENT_SECRET,
                "code": auth_code,
                "redirect_uri": settings.SOCIAL_AUTH_LINKEDIN_REDIRECT_URI,
            },
            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            timeout=5  # Set a timeout for requests
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get access token: {str(e)}"}

def get_user_info_from_linkedin(access_token):
    """Fetch GitHub user information using access token."""
    try:
        response = requests.get(
            settings.SOCIAL_AUTH_LINKEDIN_USER_INFO_URL,
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json"
            },
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get user info: {str(e)}"}
