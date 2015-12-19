from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def page_home(request):
    return render(request, "sb-agency.html")

def page_thankyou(request):
    return HttpResponse("Terima kasih")