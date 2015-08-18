from random import choice
from django.shortcuts import redirect
paises = ['Colombia', 'Peru', 'Mexico']

def de_donde_vengo(request):
    return choice(paises)
# maneja process_request o process_response
class PaisMiddleware():
    def process_request(self, request):
        pais = de_donde_vengo(request)
        if pais == 'Colombia':
            return redirect('http://icesi.edu.co')