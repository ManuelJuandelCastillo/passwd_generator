from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def passwd(request):
    caracteres = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('mayusculas'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('car-especiales'):
        caracteres.extend(list('!@#$%^&*()-_,./?><;:'))

    if request.GET.get('numeros'):
        caracteres.extend(list('0123456789'))

    passwd_length = int(request.GET.get('passwd-length'))

    passwd_generado = ''
    for caracter in range(passwd_length):
        passwd_generado += random.choice(caracteres)

    return render(request, 'passwd.html', {
        'passwd': passwd_generado
    })