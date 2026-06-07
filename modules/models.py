from django.db import models
from tinymce import models as tinymce_models 
from django.contrib.auth.models import User


class recipes(models.Model):#creatint the model so that we can enter the recipes and add it to the database
    recipe_image=models.ImageField(upload_to="recipess/",max_length=500,null=True,default=None)
    recipe_name=models.CharField(max_length=100,default=None,null=True)
    intro=tinymce_models.HTMLField()
    ingredients=tinymce_models.HTMLField()
    making=tinymce_models.HTMLField()
    nut=models.ImageField(upload_to="recipess",max_length=500,null=True,default=None)
    prep_time = models.CharField(max_length=50, null=True, default=None)
    cook_time = models.CharField(max_length=50, null=True, default=None)
    total_time = models.CharField(max_length=50, null=True, default=None)
    servings = models.IntegerField(null=True, default=None)

    def __str__(self):
        return f'{self.recipe_name}'


class chef(models.Model):
    chef_name=models.CharField(max_length=100)
    chef_age=models.PositiveIntegerField()
    chef_exp=models.CharField(max_length=500)
    chef_info=tinymce_models.HTMLField()
    chef_img=models.FileField(upload_to="chefs/",max_length=1000,null=True,default=None)
    cusine = models.CharField(max_length=100,null=True)
    nation = models.CharField(max_length=100,null = True)

    def __str__(self):
        return f'{self.chef_name} '
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} '
    
    # Create your models here.

    
