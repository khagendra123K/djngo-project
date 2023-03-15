from django.shortcuts import render
from .models import Article
from .models import Category
from .serializer import ArticleSerializer
from .serializer import CategorySerializer
from . import serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins 
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication

@api_view(['GET','POST'])
def listArticle(request):
    query = Article.objects.all()
    serializer_class = ArticleSerializer(query, many=True)
    return Response(serializer_class.data)

class ListArticles(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        query=Article.objects.all()
        serializer_Class = ArticleSerializer(query,many=True)
        return Response(serializer_Class.data)
    
    def post(self,request,pid):
        serializer_obj=ArticleSerializer(data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            product_saved=serializer_obj.save()
            return Response({"Success":"Product '{}'created successfully".format(product_saved.name)})
        return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ArticleDetaildView(APIView):

    def get(self, request,pid):
        query= Article.objects.filter(article_id=pid)
        serializer_class = ArticleSerializer(query, many=True)
        return Response(serializer_class.data)
    
    def put(self,request,pid):
        article_obj = Article.objects.get(article_id=pid)
        serializer_obj=ArticleSerializer(article_obj,data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            product_saved=serializer_obj.save()
            return Response({"Success":"Product '{}'updated successfully".format(product_saved.name)})
        return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pid):
        product_object=Article.objects.filter(article_id=pid).delete()
        return Response(status=status.HTTP_200_OK)
    
class ListArticlesMixins(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class= ArticleSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class DetailedArticleMixins(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

class ListArticleGenerics(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class DetailArticleGenerics(generics.RetrieveAPIView,
                             generics.UpdateAPIView,
                             generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class SpecailArticleGenerics(generics.ListCreateAPIView,generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ListArticlesMixins(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class=ArticleSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class DetailedArticleMixins(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

class ListArticleGenerics(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class DetailArticleGenerics(generics.RetrieveAPIView,
                             generics.UpdateAPIView,
                             generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class Category(viewsets.ModelViewSet):
 
    queryset = Category.objects.all()
    serializer_class =CategorySerializer
