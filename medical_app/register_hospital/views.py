from django.http import HttpResponse


def login(request):
    return HttpResponse("Login")


def signUp(request):
    return HttpResponse("Signup")
