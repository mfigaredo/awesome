from django.contrib import admin
from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', )

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'parent_post', )

admin.site.register(Comment, CommentAdmin)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'parent_comment', 'get_post' )

    # def get_comment(self, obj):
    #     return obj.parent_comment
    # get_comment.short_description = 'Comment'

    @admin.display(description='Post')
    def get_post(self, obj):
        return f'{obj.parent_comment.parent_post.author.username}  : {obj.parent_comment.parent_post}'
    # get_post.short_description = 'Post'

admin.site.register(Reply, ReplyAdmin)

admin.site.register(LikedPost)
admin.site.register(LikedComment)
admin.site.register(LikedReply)