from django.db import models

# Create your models here.
class Destination(models.Model):
#    previuosly used as model 
    # name:str
    # img:str
    # desc:str
    # price:int
    # offer:bool
# now being used as model for migration
    name=models.CharField(max_length=100)
    img=models.ImageField( upload_to=None)
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

# Create your models here.
