from django.contrib import admin
from .models import User, Post, Comment

class UserAdmin(admin.ModelAdmin):
    model = User

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)