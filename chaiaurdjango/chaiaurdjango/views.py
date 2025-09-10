from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, World! Welcome to Chaiaur Django Home Page!")
    return render(request, 'index.html')
def about(request):
    return HttpResponse("Hello, World! Welcome to Chaiaur Django about Page!")

def contact(request):
    return HttpResponse("Hello, World! Welcome to Chaiaur Django contact Page!") 