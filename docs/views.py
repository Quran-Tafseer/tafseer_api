from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView


class DocView(TemplateView):
    template_name = 'docs/index.html'


class IndexView(RedirectView):
    url = reverse_lazy('doc-index')
