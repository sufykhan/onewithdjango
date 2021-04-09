from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(read_only=True)
    _id=serializers.SerializerMethodField(read_only=True)
    isAdmin=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=["username","id","email","name","_id","isAdmin"]
    def get_name(self,obj):
        #first_name is comming from inbuilt user model
        name=obj.first_name
        if name=='':
            name=obj.email
        return name
    def get__id(self,obj):
        return obj.id
    def get_isAdmin(self,obj):
        return obj.is_staff

class UserSerializerWithToken(UserSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=["username","id","email","name","_id","isAdmin","token"]
    def get_token(self,obj):
        token=RefreshToken.for_user(obj)
        return str(token.access_token)