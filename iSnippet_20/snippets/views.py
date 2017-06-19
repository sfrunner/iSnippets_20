from django.shortcuts import render
from .models import Snippet
from django.http import HttpResponseRedirect
from .form import SnippetForm
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

def snippets_view(request):
    snippets = Snippet.objects.all()

    return render(request, "showSnippets.html", {"snippets_list": snippets} )