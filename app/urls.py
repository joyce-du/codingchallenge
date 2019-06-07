from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article_list'),
    path('view/<int:pk>', views.ArticleView.as_view(), name='article_view'),
]
