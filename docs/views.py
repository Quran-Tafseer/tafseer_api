from django.views.generic import TemplateView, RedirectView
from django.urls import reverse_lazy


class DocView(TemplateView):
    template_name = 'docs/index.html'


class IndexView(RedirectView):
    url = reverse_lazy('doc-index')
