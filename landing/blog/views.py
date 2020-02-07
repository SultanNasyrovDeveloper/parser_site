from django.shortcuts import render
from django.views import generic

from landing.blog import models


class PostDetail(generic.DetailView):

    queryset = models.Post.objects.all()
    template_name = 'blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()
        context['previous'] = models.Post.objects.filter(created__lt=object.created).first()
        context['next'] = models.Post.objects.filter(created__gt=object.created).first()
        return context
