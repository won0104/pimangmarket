# from django.contrib import admin
# from server.apps.posts.models import Post

# admin.site.register(Post)

# admin.py
from django.contrib import admin
from .models import Post,User
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PostResource(resources.ModelResource):
	class Meta:
		model = Post
		fields = ('id', 'title', 'user', 'content', 'price', 'region', 'photo')

class PostAdmin(ImportExportModelAdmin):
	fields = ('title', 'user', 'content', 'price', 'region', 'photo')
	list_display = ('id', 'title', 'user', 'content', 'price', 'region', 'photo')
	resource_class = PostResource

admin.site.register(Post, PostAdmin)
admin.site.register(User)