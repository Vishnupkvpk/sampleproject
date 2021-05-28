from django.contrib import admin

# Register your models here.
from api.models import Post
from api.models import Comment
from api.models import Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
