from .models import *
from rest_framework import serializers


class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = "__all__"


class StatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = "__all__"


class SiteStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = "__all__"


class HtmlHeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HtmlHeads
        fields = "__all__"


class HeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headers
        fields = "__all__"


class FootersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footers
        fields = "__all__"


class MainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mains
        fields = "__all__"


class AddedBlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddedBlocks
        fields = "__all__"


class BlockTemplatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockTemplates
        fields = "__all__"
