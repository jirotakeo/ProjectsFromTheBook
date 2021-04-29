from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefraq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmode(self, obj):
        return obj.updated
