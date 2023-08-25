from django.views import generic
from django.db.models.deletion import ProtectedError
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import JsonResponse

from django_filters.views import FilterView as OriginalFilterView
import django_filters

class ListView(generic.ListView):
    paginate_by = 50


class FilterView(OriginalFilterView):
    paginate_by = 50


class DetailView(generic.DetailView):
    # These fields will be added to the context-data.
    fields = []
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        try:
            context['fields'] = self.fields
        except AttributeError:
            pass

        return context


class CreateView(generic.CreateView):
    pass


class UpdateView(generic.UpdateView):
    pass


class DeleteView(generic.DeleteView):
    """
    Expects a reverse string for the reverse_lazy which assumes that the kwargs require a pk
    """
    model_detail_reverse_string = ''

    def get_failed_url(self, *args, **kwargs):
        obj = self.get_object()
        return reverse_lazy(self.model_detail_reverse_string, kwargs={'pk': obj.pk})

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            msg = f"Cannot delete {self.model.__name__}. There is protected information attached."
            messages.error(request, msg)
            return HttpResponseRedirect(self.get_failed_url())


class Select2ListView(ListView):
    def get_ajax_queryset(self, id):
        return self.model.objects.filter(client__id=id)

    def render_to_json_response(self, request, id, **response_kwargs):
        """
        Returns a JSON response, transforming the queryset to make the payload.
        """
        qs = self.get_queryset(id=id)
        
        return JsonResponse(
            {
                "results": [
                    {"text": obj.__str__(), "id": obj.pk}
                    for obj in qs
                ],
                "more": False,
            },
        )

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return self.render_to_json_response(request, kwargs['pk'])
        else:
            return response



class DefaultsPrepopulateFilterSetMixin:
    """
    expects a constants defaults = {'field', 'value'}
    """

    def __init__(self, *args, **kwargs):
        # Prepopulate the filter to set approved first.
        super().__init__(*args, **kwargs)

        for k, v in self.defaults.items():
            self.form.initial[k] = v


class DefaultsPrepopulateFilterViewMixin:
    """
    expects a constants defaults = {'field', 'value'}
    """

    def get_filterset_kwargs(self, filterset_class):
        # Prepopulate the qs before a filter was clicked
        kwargs = super().get_filterset_kwargs(filterset_class)
        if kwargs['data'] is None:
            kwargs['queryset'] = kwargs['queryset'].filter(**self.defaults)
        return kwargs
