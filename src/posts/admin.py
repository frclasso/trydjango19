from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","author", "update", "timestamp"]
	list_filter = ["update", "author", "title"]
	search_fields = ["content", "title"]
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)