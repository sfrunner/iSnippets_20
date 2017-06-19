"""iSnippet_20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from snippets import views as snippets_views

urlpatterns = [
    #url(r'^login/', views.login, name="login"),
    #url(r'^logout/', views.logout, name="logout"),
    url(r'^addsnippets/', snippets_views.snippets_form, name="addsnippets"),
    url(r'^snippets/', snippets_views.snippets_view, name="snippets"),
    url(r'^admin/', admin.site.urls),
]
