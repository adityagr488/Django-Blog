from django.contrib import admin
from boards import models
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp','username')
    def __str__(self):
        return self.title
admin.site.register(models.BlogPost,BlogPostAdmin)