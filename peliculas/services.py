import requests



def consumir_api(url: str):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

def ver_peliculas(parametros = {}):
    response = consumir_api('https://api.themoviedb.org/3/movie/popular?api_key=ecbcdcf9044928d12b179d9153f5a269&language=es-VE&with_genres={genres}&page={page}'.format(**parametros))

    if response:
        return response.get('results')
    
    return None

def ver_Pagina(parametros = {}):
    response = consumir_api("https://api.themoviedb.org/3/tv/popular?api_key=ecbcdcf9044928d12b179d9153f5a269&language=es-VE&with_genres={genres}28&page={page}".format(**parametros))

    if response:
        return response.get('page')
    
    return None