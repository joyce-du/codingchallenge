from django.shortcuts import render
from app.models import Article
from rest_framework import viewsets
from .serializers import ArticleSerializer

class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
