import typing

from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from landing.index import models
from landing.contact_form import forms
from landing.blog.models import Post
from landing.seo.models import PageSeo



class ContactFormProcessViewMixin(generic.FormView):

    form_class = forms.ContactForm
    success_url = None

    def form_valid(self, form):
        self.request.session['form_is_valid'] = True
        form.save()
        return redirect(self.success_url)


class IndexPageView(generic.TemplateView, ContactFormProcessViewMixin):
    """
    Index page view.
    """

    template_name = 'index.html'
    success_url = reverse_lazy('index:index')
    page_name = 'Index'

    def get_context_data(self, **kwargs) -> typing.Dict:
        """
        Add data to page context.
        """
        context = super().get_context_data(**kwargs)
        context['page'] = models.IndexPage.load()
        context['questions'] = models.FAQuestion.objects.all()
        context['examples'] = self.get_examples()
        context['categories'] = models.ParsingCategories.objects.all()
        context['posts'] = Post.objects.all()[:4]
        context['form_is_valid'] = self.request.session.get('form_is_valid', None)
        context['seo'], _ = PageSeo.objects.get_or_create(page_name=self.page_name)
        self.request.session['form_is_valid'] = None
        return context

    def get_examples(self):
        """
        Get examples for this view. If there None create.
        """
        examples = models.Example.objects.all()
        if examples.count() < 3:
            for number in range(3 - examples.count()):
                models.Example.objects.create()
        return models.Example.objects.all()[:3]


def download_document(request, example_id):
    """"""
    from sendfile import sendfile

    try:
        example = models.Example.objects.get(id=example_id)
        filepath = ''.join([settings.BASE_DIR, example.file.url])
    except models.Example.DoesNotExist:
        return redirect('index:index')

    return sendfile(request, filepath, attachment=True)




