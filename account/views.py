from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status 
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'Message':'Logout successfull'},status=status.HTTP_204_NO_CONTENT)

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()

            data['username'] = account.username
            data['email'] = account.email

            # token = Token.objects.get(use=account).key
            # data['token'] = token
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                 'refresh': str(refresh),
                 'access': str(refresh.access_token),
            }

        else:
            data = serializer.errors

        return Response(data,status.HTTP_201_CREATED)
