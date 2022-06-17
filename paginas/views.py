from django.shortcuts import render

def index(request):
    return render(request, 'paginas/index.html')

def contact(request):
    return render(request, 'paginas/contact.html')
