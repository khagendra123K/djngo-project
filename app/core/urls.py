from django.contrib import admin
from django.urls import path
from . import views
from .views import ListArticles,ListArticleGenerics,ArticleDetaildView,listArticle,ArticleViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(
    'articleviewset',ArticleViewSet,basename='Article'
)
urlpatterns = [

    path('classArticlelist/',ListArticles.as_view(), name='listproducts'),
    path('classdetailedArticle/<int:pid>/',ArticleDetaildView.as_view(), name='detailedArticle'),
    path('mixinpath/',views.ListArticleGenerics.as_view(),name='mp'),
    path('articlemixin/<int:pk>/',views.DetailArticleGenerics.as_view(),name='mdp'),
    path('articlegenericlist/',views.ListArticleGenerics.as_view(),name='lpg'),
    path('articlegenericdetail/<int:pk>/',views.DetailArticleGenerics.as_view(),name='dpg'),

    
]+router.urls
   
