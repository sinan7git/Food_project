from rest_framework.response import Response
from .serializers import FoodSerializer,FoodDetailSerializer,CartSerializer
from food.models import Food
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


@api_view(["GET"])
def food(request):
    instances = Food.objects.filter(is_deleted=False)
    q = request.GET.get("q")
    if q:
        instances = instances.filter(name__icontains=q)
    
    context = {
        "request": request
    }
    serializer = FoodSerializer(instances, many=True, context=context)
    
    response_data = {
        "status_code": 6000,
        "data": serializer.data
    }
    
    return Response(response_data)


@api_view(["GET"])
def food_detail(request,pk):
    if Food.objects.filter(pk=pk).exists():
        instance = Food.objects.get(pk=pk)
        
        context = {
            "request":request   
        }
        serializer = FoodDetailSerializer(instance,context=context)
        
        response_data = {
            "status code" : 6000,
            "data" : serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status code" : 6001,
            "message" : "Item Not Exist"
        }
        
        return Response(response_data)
    
@api_view(["GET"])
def add_cart(request):
    instance = Food.objects.filter(add_cart=True)
    context = {
        "request":request
    }
    serializer = CartSerializer(instance, many=True, context=context)
    
    response_data = {
            "status code" : 6000,
            "data" : serializer.data
        }
    return Response(response_data)


@api_view(["POST"])
def add_to_cart(request,pk):
    instance = get_object_or_404(Food, pk=pk)
    serializer = CartSerializer(instance, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save(add_cart= True)
        return Response({"status_code": 6000, "message": "Added to Cart"})
    return Response({"status_code": 6001, "message": "Validation error", "data": serializer.errors})

@api_view(["DELETE"])
def delete_cart_item(request,pk):
    instance = get_object_or_404(Food, pk=pk)
    instance.add_cart = False
    instance.save()
    return Response({"status_code": 200, "message": "Item removed from cart"})