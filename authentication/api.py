from rest_framework import generics, permissions
from .serializers import *

from rest_framework.response import Response

import requests

CLIENT_ID = 'GCqsgrJYGhNK41bKDlu7ZGc9SIhvtwnKTrbasR0n'
CLIENT_SECRET = 'xorqkdQFYD2EUd2KdUdo6IySF02iy3L8RAtkipJWq4qeeKtvLbFEdIOhbUQCJI2QLA3p5t1rmgcBNbNAwaViVxALv2x5D2dvhS0zBCRBGfbOW9OKIXhJp4BnSxAstkX2'


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        # Validate the data
        if serializer.is_valid():
            # If it is valid, save the data (creates a user).
            serializer.save()
            # Then we get a token for the created user.
            # This could be done differentley
            response = requests.post('http://127.0.0.1:8000/api/v0/o/token/',
                                     data={
                                         'grant_type': 'password',
                                         'username': request.data['username'],
                                         'password': request.data['password'],
                                         'client_id': CLIENT_ID,
                                         'client_secret': CLIENT_SECRET,
                                     },
                                     )
            return Response(response.json())
        return Response(serializer.errors)


class TokenAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        '''
        Gets tokens with username and password. Input should be in the format:
        {"username": "username", "password": "1234abcd"}
        '''
        response = requests.post(
            'http://127.0.0.1:8000/api/v0/o/token/',
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(response.json())


class RefreshTokenAPI(generics.GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        '''
        Registers user to the server. Input should be in the format:
        {"refresh_token": "<token>"}
        '''
        response = requests.post(
            'http://127.0.0.1:8000/api/v0/o/token/',
            data={
                'grant_type': 'refresh_token',
                'refresh_token': request.data['refresh_token'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(response.json())


class RevokeTokenAPI(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        '''
        Method to revoke tokens.
        {"token": "<token>"}
        '''
        response = requests.post(
            'http://127.0.0.1:8000/api/v0/o/revoke_token/',
            data={
                'token': request.data['token'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        # If it goes well return sucess message (would be empty otherwise)
        if response.status_code == requests.codes.ok:
            return Response({'message': 'token revoked'}, response.status_code)
        # Return the error if it goes badly
        return Response(response.json(), response.status_code)
