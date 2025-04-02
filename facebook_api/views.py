from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class FacebookCallback(APIView):
    def get(self, request):
        code = request.GET.get('code')
        print('code: ', code)
        if not code:
            return Response({"error": "Authorization code missing"}, status=400)
        return Response({"code": code}) 
    












# <script>
#   window.fbAsyncInit = function() {
#     FB.init({
#       appId      : '{your-app-id}',
#       cookie     : true,
#       xfbml      : true,
#       version    : '{api-version}'
#     });
      
#     FB.AppEvents.logPageView();   
      
#   };

#   (function(d, s, id){
#      var js, fjs = d.getElementsByTagName(s)[0];
#      if (d.getElementById(id)) {return;}
#      js = d.createElement(s); js.id = id;
#      js.src = "https://connect.facebook.net/en_US/sdk.js";
#      fjs.parentNode.insertBefore(js, fjs);
#    }(document, 'script', 'facebook-jssdk'));
# </script>



# FB.getLoginStatus(function(response) {
#     statusChangeCallback(response);
# });



# {
#     status: 'connected',
#     authResponse: {
#         accessToken: '...',
#         expiresIn:'...',
#         signedRequest:'...',
#         userID:'...'
#     }
# }



# <fb:login-button 
#   scope="public_profile,email"
#   onlogin="checkLoginState();">
# </fb:login-button>



# function checkLoginState() {
#   FB.getLoginStatus(function(response) {
#     statusChangeCallback(response);
#   });
# }

# https://c0b0-103-250-149-229.ngrok-free.app/facebook/callback/
# http://127.0.0.1:8000/facebook/callback/