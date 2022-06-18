from django.shortcuts import render

def index(request):
    return render(request, 'paginas/index.html')

# SOBRE
# 

# CURSOS
# 

# EVENTOS
# 

def laboratories(request):
    return render(request, 'paginas/laboratories.html')

def instructors(request):
    return render(request, 'paginas/instructors.html')

def certification(request):
    return render(request, 'paginas/certification.html')

def contact(request):
    return render(request, 'paginas/contact.html')