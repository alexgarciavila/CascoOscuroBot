import requests
from bs4 import BeautifulSoup as bs


def preparar_sopa(urlguild):
    """ Preparación de la sopa para scrapear """
    r = requests.get(urlguild, timeout=5)
    soup = bs(r.text, "html.parser")
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
        valor = item.find("div", class_="stat-item-value").text.strip()
        items[item.find("div", class_="stat-item-title").text.strip()] = valor

    return items


def scrap_miembros_guild(soup):
    """
        Escrapeamos a todos los miembros del gremio
    """
    find_members = soup.find_all("tr")
    miembros = {}
    titulos = scrap_titulos(find_members)

    for miembro in find_members:
        stats = miembro.find_all("td")
        for stat in stats:
            nom_miembro = scrap_nom_miembro(stat)
            if nom_miembro is not None:
                if nom_miembro not in miembros:
                    miembros[nom_miembro] = {}
                    last_member = nom_miembro
                    contador = 1
                    miembros[last_member]["URL"] = scrap_url_miembro(stat)
            else:
                miembros[last_member][titulos[contador]] = stat.text.strip()
                contador += 1
    return miembros


def scrap_titulos(find_titulos):
    """
    En esta función scrapeamos los titulos de la tabla de miembros
    """
    clean_titles = []
    for titulo in find_titulos:
        titulos = titulo.find_all("th")
        for t in titulos:
            clean_titles.append(t.text.strip())

    return clean_titles


def scrap_nom_miembro(find_nombre):
    """
    Comprobamos si es un nombre de un miembro del gremio o no
    """
    if find_nombre.find("strong"):
        nom_miembro = find_nombre.find("strong").text.strip()

        return nom_miembro


def scrap_url_miembro(find_url):
    """
    Extraemos la url de cada miembro de swgoh.gg
    """
    url_swgohgg = "https://swgoh.gg"
    url_miembro = ""

    url_miembro = find_url.find("a", href=True)
    url = url_swgohgg + url_miembro["href"]

    return url
