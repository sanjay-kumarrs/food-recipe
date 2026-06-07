from django.contrib import admin
from modules.models import recipes
from modules.models import chef
from .models import UserProfile

admin.site.register(UserProfile)

class fooding(admin.ModelAdmin):
    list_display=('recipe_name','intro','prep_time','cook_time','total_time','servings','ingredients','making','nut','recipe_image')
    search_fields=('recipe_name',)

class chefs(admin.ModelAdmin):
    list_display=('chef_name','chef_age','chef_exp','chef_info','chef_img','cusine','nation')
    search_fields=('chef_name',)



admin.site.register(recipes,fooding)
admin.site.register(chef,chefs)#if we want to display the model in admin we have to register it here
# Register your models here.
