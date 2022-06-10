from multiprocessing import context
from pathlib import Path
from django.views.generic import View
from django.shortcuts import render
from django.views.defaults import page_not_found
import sys
from django.core import management
from django.apps import apps
from django.contrib.auth.decorators import login_required
from core.forms import UploadForm

def home(request):
    context={}
    return render(request, 'pages/index.html', context)

def manual(request):
    context= {}
    return render(request, 'help.html', context)


def error_404(request, exception):
    return render(request, '404.html')


def crear_archivos(app_name): 
    myfile = Path(f"static/backup/{app_name}.json")
    myfile.touch(exist_ok=True)
def extraer_datos(appname):
    for i in range (2):
        sysout = sys.stdout 
        sys.stdout = open(f"static/backup/{appname}.json", "w+")
        management.call_command('dumpdata', appname, indent=4, format='json')
        
def subir_datos(app_name, f):
    with open(f"static/backup/{app_name}.json", "wb+") as destination:
        for chunck in f.chunck():
            destination.write(chunck)
            
@login_required(login_url='/login/')  
def backup(request):
    modelos = list(map(lambda x: x._meta, apps.get_models()[12:]))
    filtrado = []
    if request.method == 'post':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            subir_datos(request.post['title'],request.FILES['file'])
            print ("si funciona")
            
    elif request.method == 'POST':
        for modelo in modelos :
            if modelo.verbose_name in request.POST.getlist("modelos_lista"):
                filtrado.append(modelo)
            print (filtrado)
    for i in filtrado:
        crear_archivos(i)
        extraer_datos(i)
    else:
        pass
    context = {"modelos":modelos}
    return render(request, 'backup.html', context)