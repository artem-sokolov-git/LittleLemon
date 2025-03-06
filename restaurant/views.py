from django.http import HttpRequest, HttpResponse


def say_welcome(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello world")
