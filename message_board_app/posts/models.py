from django.db import models

# Create your models here.
class Post(models.Model):
    
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    message = models.TextField()
    
    
    def __str__(self) -> str:
        return self.message[:90]