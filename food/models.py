from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=50)
    image =models.ImageField(upload_to="products/images/")
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey("food.Category",on_delete=models.CASCADE,null=True)
    add_cart = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    def __str__ (self):
        return self.name
        
    
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name