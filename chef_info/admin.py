from django.contrib import admin

from chef_info.models import feedBack



class feedback(admin.ModelAdmin):
    list_display=('name','email','subject','message')

class feeds(admin.ModelAdmin):
    list_display = ('f_id','chef_name','feedback_date','feedback','reply')


admin.site.register(feedBack,feedback)

