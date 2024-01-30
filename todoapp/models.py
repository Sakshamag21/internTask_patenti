from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null= True)
    priority = models.IntegerField()
    endDate=models.DateField()
    status=models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
