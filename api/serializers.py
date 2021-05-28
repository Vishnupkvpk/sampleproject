from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post
from api.models import Comment
from api.models import Category
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    owner =   serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Category    
        fields = ['id', 'name', 'owner', 'posts']
        
class PostSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #comments = serializers.CharField(source='comments.body')
    #categories = CategorySerializer(many=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'image', 'owner', 'comments', 'categories']
        
      
    #     class PostSerializer(WritableNestedModelSerializers,serializers.ModelSerializer):
    #     owner = serializers.ReadOnlyField(source='owner.username')
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # #comments = serializers.CharField(source='comments.body')
    # categories = CategorySerializer(source='categories',many=True)
    # class Meta:
    #     model = Post
    #     fields = ['id', 'title', 'body', 'owner', 'comments', 'categories']
        # def create(self, validated_data):
        #     categories_data = validated_data.pop('categories')
        #     post= Post.objects.create(**validated_data)
        #     for category_data in categories_data:
        #         Category.objects.create(post=post, **category_data)
        #     return post
        #depth =6

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments', 'categories']
       

class CommentSerializer(serializers.ModelSerializer):
    owner =   serializers.ReadOnlyField(source='owner.username')
    #post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    
    class Meta:
        model = Comment     
        fields = ['id', 'body', 'owner', 'post']
