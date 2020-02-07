from django.db import models


class BasePageSeo(models.Model):
    title = models.CharField('Title', max_length=250, null=True, blank=True)
    keywords = models.CharField('Keywords', max_length=500, null=True, blank=True)
    description = models.CharField('Description', max_length=500, null=True, blank=True)
    raw_html = models.TextField('Raw html', null=True, blank=True)

    class Meta:
        abstract = True


class PageSeo(BasePageSeo):
    page_name = models.CharField('Page name', max_length=100)

    def __str__(self):
        return f'{self.page_name} page seo'


class PostSeo(BasePageSeo):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='page_seo')

    def __str__(self):
        return f'{self.post.name} seo'
