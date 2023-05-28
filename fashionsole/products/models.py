from django.db import models

# Create your models here.

class category(models.Model):
    catimge=models.ImageField(upload_to="pic")
    type=models.CharField(max_length=100)

    def __str__(self):
        return self.type

class products(models.Model):
    brandname=models.CharField(max_length=100)
    productname=models.TextField()
    img=models.ImageField(upload_to="pic")
    discprice=models.CharField(max_length=10)
    disc=models.CharField(max_length=5)
    price=models.CharField(max_length=10)
    size=models.IntegerField()
    type=models.ForeignKey(category,on_delete=models.CASCADE, default=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.type)





