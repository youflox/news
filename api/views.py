from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ArticlesListSerializer, ArticleDetailSerializer
from .models import Article


class ArticlesListApiview(APIView):
    def get(self, request):
        articles    = Article.objects.all()
        serializer  = ArticlesListSerializer(articles, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ArticlesDetailsApiveiw(APIView):
    def get(self, request, *args, **kwargs):
        article     = Article.objects.get(slug=kwargs['slug'])
        serializer  = ArticleDetailSerializer(article)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
