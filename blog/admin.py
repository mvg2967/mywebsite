from django.contrib import admin
from blog.models import Post, Comment, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	exclude = ['posted']
	prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
	display_fields = ["post", "author", "created"]

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
