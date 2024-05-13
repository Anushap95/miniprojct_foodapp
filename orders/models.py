from django.db import models  


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    Image = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name




    
