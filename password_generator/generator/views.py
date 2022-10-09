import string, random
from django.shortcuts import render



# Create your views here.

def generate_password(request):

    context = {

    }
    return render(request, template_name='generator/gen.html', context={})

def password(request):
    pwd = ''
    length = int(request.GET.get('length'))
    chars = string.ascii_lowercase
    if request.GET.get('uppercase'):
        chars += string.ascii_uppercase
    if request.GET.get('numbers'):
        chars += string.digits
    if request.GET.get('special'):
        chars += string.punctuation
    for i in range(length):
        pwd += random.choice(chars)
    return render(request, template_name='generator/password.html', context={'length':length, 'pwd':pwd})


def sorry(request):
    return render(request, template_name='generator/something_went_wrong.html')