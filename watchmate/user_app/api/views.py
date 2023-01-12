from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from user_app.api.serializers import RegistrationSerializer
from user_app import models


@api_view(['POST'])
def user_logout(request):
    
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'detail':'User logout successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def user_registration(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['Response'] = 'Registration succefully!'
            data['username'] = account.username
            data['email'] = account.email
            
            # generate the token automatically for valid user   -> import the Token class
            token = Token.objects.get(user = account).key
            data['token'] = token
        
        else:
            data = serializer.errors
        
        return Response(data)
        
        