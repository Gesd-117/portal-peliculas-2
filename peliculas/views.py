from django.shortcuts import render
from typing import Dict, Any
from .services import ver_peliculas, ver_Pagina

# Create your views here.

def inicio(request, page: int = 1):

    parametros : Dict[str, Any] = {
        'genres': '28',
        'page': page,
    }
    datos: Dict[str, Any] = {
        'titulo': 'Portal de Peliculas',
        'encabezado': 'Listado de peliculas',
        'peliculas': ver_peliculas(parametros),
        'images': 'https://image.tmdb.org/t/p/w500',
        'pagina_actual': ver_Pagina(parametros),
    }
    
    return render(request, 'peliculas/index.html', datos)

def anterior(request, page):
    
    nueva_pagina: int = max(1, page - 1) 
    
    return inicio(request,nueva_pagina)


def siguiente(request, page):
    nueva_pagina: int = page + 1
    return inicio(request,nueva_pagina)
    