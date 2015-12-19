from django.conf.urls import url
from peminjaman.views import PustakaList

urlpatterns = [
    url(r'^$', PustakaList.as_view(), name="pustaka-list")
]