from django.views.generic.list import ListView
from .models import Snippet

class SnippetDetailView(ListView):

    model = Snippet

    def get_context_data(self, **kwargs):
        context = super(SnippetDetailView,
    self).get_context_data(**kwargs)
        return context