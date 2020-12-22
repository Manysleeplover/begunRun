from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
     list_display = ('id', 'author', 'calories', 'pace', 'time', 'distance', 'text_train', 'photo', 'date')
     list_display_links = ('calories', 'pace', 'time', 'distance', 'text_train', 'photo',)
     search_fields = ('author', 'id')





# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#      list_display = ('datetime', 'author', 'post', 'text')
#      list_filter = ('datetime', 'author')
#      search_fields = ('author', 'body')
