from django.views.generic.base import TemplateView
from django.http import Http404

from api import v1
from .models import Book

class IndexView(TemplateView):
    template_name = 'index.html'


class DetailView(TemplateView):
    template_name = 'index.html'

    def get_detail(self, pk):
        tr = v1.canonical_resource_for('book')

        try:
            book = tr.cached_obj_get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

        bundle = tr.full_dehydrate(tr.build_bundle(obj=book))
        data = bundle.data
        return data

    def get_context_data(self, **kwargs):
        base = super(DetailView, self).get_context_data(**kwargs)
        base['data'] = self.get_detail(base['params']['pk'])
        return base
