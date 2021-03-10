from django.contrib import admin

# Register your models here.
from home.models import Contact,Author

admin.site.register(Contact)
admin.site.register(Author)