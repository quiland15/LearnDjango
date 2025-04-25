from django.http import HttpResponse

def url(request):
    return HttpResponse("Hallo World")

def blog(request):
    return HttpResponse("ini halaman blog")