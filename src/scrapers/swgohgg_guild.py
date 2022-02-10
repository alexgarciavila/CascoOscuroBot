from optparse import Values
import requests
from bs4 import BeautifulSoup as bs
import re

def preparar_sopa(urlguild):
    """ Preparación de la sopa para scrapear """
    r=requests.get(urlguild, timeout=5)
    soup = bs(r.text,"html.parser")
    return soup



def nombre_gremio(soup):
    """
    Función para scrapear el nombre de la guild 

    Buscamos el tag h1, pero como el nombre del gremio no tiene tag,
    y al pasarlo a texto nos incluye el contenido del tag small, 
    entonces buscamos el tag small y lo eliminamos para que no nos
    lo incluya.
    Luego eliminamos los espacios en blanco que ha creado el descompose    
    
    """

    find_nombre = soup.find("h1")
    for h1 in find_nombre.find_all("small"):
        h1.decompose()

    nombre = find_nombre.text
    nombre = nombre.strip("\n")

    return nombre

def activos(soup):
    """
    Función para scrapear los usuarios activos en swgoh.gg

    Se deberia mejorar la función seprando los activos del total 
    NO FUNCIONA    
    """

    find_activos = soup.find("h1")
    print(find_activos)
    for h1 in find_activos.find_all("small"):
        num_activos = find_activos.text
        print(num_activos)

    return num_activos

def scrap_items_guild(soup):
    """
        Añadimos a un diccionario todos los datos del gremio
    """
 
    find_items = soup.find_all("div", class_="stat-item-info")
    items = {}
    for item in find_items:
        items[item.find("div", class_="stat-item-title").text.strip()] = item.find("div", class_="stat-item-value").text.strip()

    return items
    
def scrap_miembros_guild(soup):
    """
        Escrapeamos a todos los miembros del gremio
    """
    find_members = soup.find_all("tr")
    miembros = {}
    valores = []
    for miembro in find_members:
        #if miembro.find("strong"):
        #    miembros.append(miembro.find("strong").text.strip())
            #miembros[miembro.find("strong").text.strip()] = miembro.find("small").text.strip()
        stats = miembro.find_all("td")
        for stat in stats:
            if stat.find("strong"):
                key = stat.find("strong").text.strip()
            else:
                value = stat.text.strip()
                valores.append(value)

            if key not in miembros:
                miembros[key] = list()
                valores = []
            miembros[key] = valores
    return miembros