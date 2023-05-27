from rest_framework.serializers import ModelSerializer
from food.models import Food
from rest_framework import serializers


class FoodSerializer(ModelSerializer):
    
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = Food
        fields = ('id','name','image','price','category')
        
        
    def get_category(self, instance):
        return instance.category.name
        
        
class FoodDetailSerializer(ModelSerializer):
    
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = Food
        fields = ('id','name','image','price','category')
        
        
    def get_category(self, instance):
        return instance.category.name
        
        
class CartSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = ("id","image","name","price","category","description")