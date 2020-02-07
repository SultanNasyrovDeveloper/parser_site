from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from landing.blog import models
from landing.seo.models import PostSeo
from landing.index.views import ContactFormProcessViewMixin


class PostDetail(generic.DetailView, ContactFormProcessViewMixin):

    queryset = models.Post.objects.all()
    template_name = 'blog_detail.html'
    context_object_name = 'post'

    @property
    def success_url(self):
        return reverse_lazy('blog:detail', args=(self.get_object().id, ))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()
        context['seo'], _ = PostSeo.objects.get_or_create(post=self.get_object())
        context['previous'] = models.Post.objects.filter(created__lt=object.created).first()
        context['next'] = models.Post.objects.filter(created__gt=object.created).first()
        return context
