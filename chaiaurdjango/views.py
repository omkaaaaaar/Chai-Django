from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World! Welcome to Chaiaur Django Home Page!")

def about(request):
    return HttpResponse("Hello, World! Welcome to Chaiaur Django about Page!")

def contact(request):
    return HttpResponse("Hello, World! Welcome to Chaiaur Django contact Page!") 