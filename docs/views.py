from django.views.generic import TemplateView


class DocView(TemplateView):
    template_name = 'docs/index.html'
