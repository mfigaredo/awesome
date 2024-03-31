from django.template import Library
from django.db.models import Count
from ..models import Tag, Post, Comment

register = Library()

@register.inclusion_tag('includes/sidebar.html')
def sidebar_view(tag=None, user=None):
    categories = Tag.objects.all()
    top_posts = Post.objects.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by('-num_likes')[:5]
    top_comments = Comment.objects.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by('-num_likes')[:5]
    context = {
        'categories': categories,
        'tag': tag,
        'top_posts': top_posts,
        'user': user,
        'top_comments': top_comments,
    }
    return context
