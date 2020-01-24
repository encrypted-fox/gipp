from rest_framework import viewsets, permissions
from .serializers import *


class SitesViewSet(viewsets.ModelViewSet):
    queryset = Sites.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SitesSerializer


class StatusesViewSet(viewsets.ModelViewSet):
    queryset = Statuses.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StatusesSerializer


class SiteStatusesViewSet(viewsets.ModelViewSet):
    queryset = SiteStatuses.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SiteStatusesSerializer


class HtmlHeadsViewSet(viewsets.ModelViewSet):
    queryset = HtmlHeads.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HtmlHeadsSerializer


class HeadersViewSet(viewsets.ModelViewSet):
    queryset = Headers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HeadersSerializer


class FootersViewSet(viewsets.ModelViewSet):
    queryset = Footers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FootersSerializer


class MainsViewSet(viewsets.ModelViewSet):
    queryset = Mains.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MainsSerializer


class AddedBlocksViewSet(viewsets.ModelViewSet):
    queryset = AddedBlocks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AddedBlocksSerializer


class BlockTemplatesViewSet(viewsets.ModelViewSet):
    queryset = BlockTemplates.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BlockTemplatesSerializer
