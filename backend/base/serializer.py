from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
class UserSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=["username","id","email","name"]
    def get_name(self,obj):
        #first_name is comming from inbuilt user model
        name=obj.first_name
        if name=='':
            name=obj.email
        return name
