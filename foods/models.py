from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50) #charfield로 모든 모델은 필드를 정해줘야함
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name