"""perpus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


## url admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) ## serve static assets

## pages
from pages import views as pages_views
urlpages = [
    url(r'^$', pages_views.page_home, name="home"),
    url(r'^thankyou/$', pages_views.page_thankyou, name="thankyou"),
]
urlpatterns += urlpages
## url perpustakaan
urlperpustakaan = [
    url(r'^perpustakaan/', include('peminjaman.urls', namespace="perpustakaan", app_name="peminjaman"))
]
urlpatterns += urlperpustakaan
## url blogs 
urlblogs = [
    url(r'^blogs/', include('blogs.apps', namespace="blogs", app_name="blogs"))
]
urlpatterns += urlblogs