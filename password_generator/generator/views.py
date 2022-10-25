from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')


def password_generator(request):
    return render(request, 'generator/password-generator.html')


def password(request):
    passW = generate_password(request)
    return render(request, 'generator/password.html', {'password': passW})


def about(request):

    return render(request, 'generator/about.html')

def generate_password(request):
    try:
        characters = list()

        if request.GET.get('uppercase'):
            characters.extend(passwordElements('uppercase'))

        if request.GET.get('lowercase'):
            characters.extend(passwordElements('lowercase'))

        if request.GET.get('specialChar'):
            characters.extend(passwordElements('specialChar'))

        if request.GET.get('numbers'):
            characters.extend(passwordElements('numbers'))

        length = int(request.GET.get('length'))

        passW = ''

        for x in range(length):
            passW += random.choice(characters)
    except:
        passW = 'ERROR: Select an option'
    return passW

def passwordElements(element):
    dictionary = {'uppercase': list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'lowercase': list('abcefghijklmnopqrstuvwxyz'), 'numbers': list('0123456789'), 'specialChar': list(')_+="\:;&/~!$%^.*@#(|?><')}

    return dictionary[element]