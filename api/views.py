from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from api import serializers
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination 
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from api.permissions import IsOwnerReadOnly
from django.contrib.auth.models import User
from api.models import Post
from api.models import Comment
from api.models import Category

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
# class Logout(APIView):
#     def get(self, request, format=None):
#         # simply delete the token to force a login
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','body','owner__username']
    pagination_class = PageNumberPagination
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerReadOnly]
    

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerReadOnly]   
    
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerReadOnly] 