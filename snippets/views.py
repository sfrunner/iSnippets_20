from django.shortcuts import render
from .models import Snippet
from django.http import HttpResponseRedirect
from .form import SnippetForm
from django.views.generic.list import ListView
from django.forms import modelformset_factory

# Create your views here.

#import snippets to render

def snippets_form(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid(): 
            form_instance = Snippet(title = request.POST.get("snippet_title",""),language = request.POST.get("snippet_language",""), codeSnippet = request.POST.get("snippet_code", ""), description = request.POST.get("snippet_description",""), author = request.POST.get("snippet_author",""))
            form_instance.save()
            return HttpResponseRedirect("/snippets/")
            
    else: 
        form = SnippetForm()
    return render(request, "addSnippets.html", {"form": form})

class SnippetDetailView(ListView):

    model = Snippet
    context_object_name = "snippets_list"
    queryset = Snippet.objects.all()
    template_name = "showSnippets.html"

def delete(request, snippet_id):
    query = Snippet.objects.get(id=snippet_id)
    query.delete()
    return HttpResponseRedirect("/snippets/")

def manage_snippets(request):
    SnippetFormSet = modelformset_factory(Snippet, fields=('title', 'language', 'codeSnippet', 'description', 'author'))
    if request.method == 'POST':
        formset = SnippetFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
            return HttpResponseRedirect("/updatesnippets/")
    else:
        formset = SnippetFormSet()
    return render(request, 'manageSnippets.html', {'formset': formset})