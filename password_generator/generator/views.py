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

    characters = list()
    print("hello world")
    print(request.GET)
    json = request.GET
    flag = 'on'
    password_length = json['pass_size']
    if json.get('uppercase') == flag:
        characters.extend(passwordElements('uppercase'))

    if json.get('lowercase') == flag:
        characters.extend(passwordElements('lowercase'))

    if json.get('specialChar') == flag:
        characters.extend(passwordElements('specialChar'))

    if json.get('numbers') == flag:
        characters.extend(passwordElements('numbers'))

    if len(characters) == 0:
        passW = "Error: Please select an option"
        return passW
    passW = ''
    print(password_length)
    for x in range(int(password_length)):
        passW += random.choice(characters)

    return passW


def passwordElements(element):
    dictionary = {'uppercase': list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'lowercase': list(
        'abcefghijklmnopqrstuvwxyz'), 'numbers': list('0123456789'), 'specialChar': list(')_+="\:;&/~!$%^.*@#(|?><')}

    return dictionary[element]
