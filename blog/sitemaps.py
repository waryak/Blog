from .models import Post
from django.contrib.sitemaps import Sitemap


# Sitemaps are not switched on - refer to a book page 76

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated