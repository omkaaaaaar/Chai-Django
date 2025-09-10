from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, World! Welcome to Chaiaur Django Home Page!")
    return render(request, 'website/index.html')
def about(request):
    #return HttpResponse("Hello, World! Welcome to Chaiaur Django about Page!")
    return render(request, 'about/about.html')
def contact(request):
   # return HttpResponse("Hello, World! Welcome to Chaiaur Django contact Page!") 
   return render(request, 'contact/contact.html')