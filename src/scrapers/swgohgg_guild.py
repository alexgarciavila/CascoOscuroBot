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


def comparar_gremio(guild, guild2, nombre_guild, nombre_guild2):
    """
    Obtenemos los datos de dos gremios y los comparamos.
    Mostramos un resumen de las conclusiones

    TENEMOS QUE REFACTORIZAR TODOS ESOS IF
    """
    txt_g1 = (
              "\nGremio {name_1}\n"
              "Galactic Power: {gp_1}\n"
              "Media de GP: {avggp_1}\n\n"
              "Leyendas Galácticas\n"
              "REY: {rey_1}\n"
              "Supreme Leader Kylo Ren: {slkr_1}\n"
              "Jedi Master Luke: {jml_1}\n"
              "Sith Eternal Emperor: {see_1}\n"
              "Jedi Master Kenobi: {jmk_1}\n"
              "Lord Vader: {lv_1}\n\n"
              ).format(
                       name_1=nombre_guild,
                       gp_1=guild.gp,
                       avggp_1=guild.avggp,
                       rey_1=guild.rey,
                       slkr_1=guild.slkr,
                       jml_1=guild.jml,
                       see_1=guild.see,
                       jmk_1=guild.jmk,
                       lv_1=guild.lv,
              )
    txt_g2 = (
              "\nGremio {name_2}\n"
              "Galactic Power: {gp_2}\n"
              "Media de GP: {avggp_2}\n\n"
              "Leyendas Galácticas\n"
              "REY: {rey_2}\n"
              "Supreme Leader Kylo Ren: {slkr_2}\n"
              "Jedi Master Luke: {jml_2}\n"
              "Sith Eternal Emperor: {see_2}\n"
              "Jedi Master Kenobi: {jmk_2}\n"
              "Lord Vader: {lv_2}\n\n"
              ).format(
                       name_2=nombre_guild2,
                       gp_2=guild2.gp,
                       avggp_2=guild2.avggp,
                       rey_2=guild2.rey,
                       slkr_2=guild2.slkr,
                       jml_2=guild2.jml,
                       see_2=guild2.see,
                       jmk_2=guild2.jmk,
                       lv_2=guild2.lv,
              )
    rey_comp = int(guild.rey) - int(guild2.rey)
    slkr_comp = int(guild.slkr) - int(guild2.slkr)
    jml_comp = int(guild.jml) - int(guild2.jml)
    see_comp = int(guild.see) - int(guild2.see)
    jmk_comp = int(guild.jmk) - int(guild2.jmk)
    lv_comp = int(guild.lv) - int(guild2.lv)

    # REY LG
    if rey_comp < 0:
        txt_rey = (
                   "Tenemos {rey} REYS menos que el otro gremio\n"
                  ).format(
                      rey=abs(rey_comp)
                  )
    elif rey_comp > 0:
        txt_rey = (
                   "Tenemos {rey} REYS más que el otro gremio\n"
                  ).format(
                      rey=abs(rey_comp)
                  )
    else:
        txt_rey = "Tenemos las mismas REYS que el otro gremio\n"

    # SLKR LG
    if slkr_comp < 0:
        txt_slkr = (
                   "Tenemos {slkr} Supreme Leader Kylo Ren "
                   "menos que el otro gremio\n"
                  ).format(
                      slkr=abs(slkr_comp)
                  )
    elif slkr_comp > 0:
        txt_slkr = (
                   "Tenemos {slkr} Supreme Leader Kylo Ren "
                   "más que el otro gremio\n"
                  ).format(
                      slkr=abs(slkr_comp)
                  )
    else:
        txt_slkr = (
                    "Tenemos los mismos Supreme Leader Kylo Ren "
                    "que el otro gremio\n"
                    )

    # JML
    if jml_comp < 0:
        txt_jml = (
                   "Tenemos {jml} Jedi Master Luke menos que el otro gremio\n"
                  ).format(
                      jml=abs(jml_comp)
                  )
    elif jml_comp > 0:
        txt_jml = (
                   "Tenemos {jml} Jedi Master Luke más que el otro gremio\n"
                  ).format(
                      jml=abs(jml_comp)
                  )
    else:
        txt_jml = "Tenemos los mismos Jedi Master Luke que el otro gremio\n"

    # SEE
    if see_comp < 0:
        txt_see = (
                   "Tenemos {see} Sith Eternal Emperor "
                   "menos que el otro gremio\n"
                  ).format(
                      see=abs(see_comp)
        )
    elif see_comp > 0:
        txt_see = (
                   "Tenemos {see} Sith Eternal Emperor "
                   "más que el otro gremio\n"
                  ).format(
                      see=abs(see_comp)
        )
    else:
        txt_see = (
                    "Tenemos los mismos Sith Eternal Emperor "
                    "que el otro gremio\n"
        )

    # JMK
    if jmk_comp < 0:
        txt_jmk = (
                   "Tenemos {jmk} Jedi Master Kenobi menos "
                   "que el otro gremio\n"
                  ).format(
                      jmk=abs(jmk_comp)
                  )
    elif jmk_comp > 0:
        txt_jmk = (
                   "Tenemos {jmk} Jedi Master Kenobi más que el otro gremio\n"
                  ).format(
                      jmk=abs(jmk_comp)
                  )
    else:
        txt_jmk = "Tenemos los mismos Jedi Master Kenobi que el otro gremio\n"

    # LV
    if lv_comp < 0:
        txt_lv = (
                   "Tenemos {lv} Lord Vader menos que el otro gremio\n"
                  ).format(
                      lv=abs(lv_comp)
                  )
    elif lv_comp > 0:
        txt_lv = (
                   "Tenemos {lv} Lord Vader más que el otro gremio\n"
                  ).format(
                      lv=abs(lv_comp)
                  )
    else:
        txt_lv = "Tenemos los mismos Lord Vader que el otro gremio\n"

    print(txt_g1, txt_g2, txt_rey, txt_slkr, txt_jml, txt_see, txt_jmk, txt_lv)
