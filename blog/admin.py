from django.contrib import admin
from blog.models import Post,BlogComment
# Register your models here.
admin.site.register((BlogComment))

@admin.register(Post) #decorator to register my post at admin and also some change  in my post template
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
