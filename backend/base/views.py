from django.shortcuts import render

from rest_framework.decorators import api_view

from rest_framework.response import Response

from .productsData import products
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    return Response({"message":"high"})
@api_view(['GET'])
def getProducts(request):
    return Response(products)
@api_view(['GET'])
def getProduct(request,pk):
    product=None
    for i in products:
        if i['_id']==pk:
            product=i
            break
    return Response(product)
