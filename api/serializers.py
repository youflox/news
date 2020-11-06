from rest_framework import serializers


class ArticlesListSerializer(serializers.Serializer):
    id          = serializers.IntegerField()
    title       = serializers.CharField()
    description = serializers.CharField()
    author      = serializers.CharField()
    date        = serializers.DateTimeField()
    image       = serializers.ImageField()
    slug        = serializers.CharField()

class ArticleDetailSerializer(serializers.Serializer):
    title       = serializers.CharField()
    description = serializers.CharField()
    paragraph   = serializers.CharField()
    author      = serializers.CharField()
    date        = serializers.DateTimeField()
    image       = serializers.ImageField()
