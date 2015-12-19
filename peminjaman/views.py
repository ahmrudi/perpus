from django.views import generic
from peminjaman import models


class PustakaList(generic.ListView):
    model = models.Pustaka