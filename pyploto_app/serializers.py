from .models import User, Post, Comment
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id','email','first_name','last_name','username','password','profile_picture')
        extra_kwargs = {'write_only': True}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_id','author', 'title', 'media', 'caption','datetime_modified')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','post_id', 'author_id', 'body')