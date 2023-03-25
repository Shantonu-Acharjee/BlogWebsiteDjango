from django.contrib import admin
from . models import Category, Post


# for configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'descriptions', 'url', 'add_date')
    search_fields = ('title',)



# for configuration of post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'url')
    search_fields = ('title',)
    list_filter = ('cat',)




# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)