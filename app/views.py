from django.shortcuts import HttpResponse, render

def home(request):
    if request.user.is_authenticated:
        return HttpResponse("Working")
    else:
        return HttpResponse("Not loged In")

