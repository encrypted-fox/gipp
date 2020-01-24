from rest_framework import viewsets, permissions
from .serializers import *


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = Posts
    permissions = [permissions.IsAuthenticated]
    queryset = Posts.objects.all()
