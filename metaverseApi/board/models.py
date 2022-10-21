from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length = 100, default="")
    writer = models.CharField(max_length = 20, default="")
    create_date = models.DateField(auto_now_add=True)
    count = models.IntegerField(default=0)
    recommend = models.IntegerField(default=0)
    password = models.CharField(max_length = 40, default="")
    contents = models.CharField(max_length = 2000, default ="")

    class Meta:
        ordering = ['-id']