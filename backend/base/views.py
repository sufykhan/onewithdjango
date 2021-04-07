from django.shortcuts import render

from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer
from .productsData import products
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username
        return token
    def validate(self,user):
        data=super().validate(user)
        data["username"]=self.user.username
        data["email"]=self.user.email
        return data

#This is for returning extra information decoded in the token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    return Response({"message":"high"})

@api_view(['GET'])
def getProducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
    product=Product.objects.get(_id=pk)
    serializer=ProductSerializer(product,many=False)
    #serializer.data is in the form of dictionary
    return Response(serializer.data)
