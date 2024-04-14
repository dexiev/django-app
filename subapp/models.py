from django.db import models

from cloudinary.models import CloudinaryField
# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table='post'
        
    name=models.CharField(
        'name', max_length=160, blank=False, null=False,default="anonymous"
    )

    body=models.CharField(
        "Body", max_length=600, blank=False, null= False, default="YOUR BODY HERE"
    )

    created_at=models.DateTimeField('created_at', auto_now_add=True)  


    image= CloudinaryField(
        'image', blank= True
    )  

    likes=models.PositiveIntegerField(
        'Likes', default=0, blank=True
    )


    # dislikes=models.PositiveIntegerField(
    #     "Dislikes", default=0, blank=True
    # )