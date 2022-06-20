from django.shortcuts import render

def index(request):
    return render(request, 'paginas/index.html')

# SOBRE
def ict_academy(request):
    return render(request, 'paginas/sobre/ict-academy.html')

def huawei(request):
    return render(request, 'paginas/sobre/huawei.html')
# 

# CURSOS
def cincoG_networks(request):
    return render(request, 'paginas/cursos/5g-networks.html')

def artificial_intelligence(request):
    return render(request, 'paginas/cursos/artificial-intelligence.html')

def cloud_service(request):
    return render(request, 'paginas/cursos/cloud-service.html')

def datacom(request):
    return render(request, 'paginas/cursos/datacom.html')

# 

# EVENTOS
def ict_competition_brasil(request):
    return render(request, 'paginas/eventos/ict-competition-brasil.html')

def ict_job_fair_brasil(request):
    return render(request, 'paginas/eventos/ict-job-fair-brasil.html')

def seeds_fot_the_future(request):
    return render(request, 'paginas/eventos/seeds-for-the-future.html')

# 

def laboratories(request):
    return render(request, 'paginas/laboratories.html')

def instructors(request):
    return render(request, 'paginas/instructors.html')

def certification(request):
    return render(request, 'paginas/certification.html')

def contact(request):
    return render(request, 'paginas/contact.html')