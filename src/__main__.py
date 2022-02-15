from scrapers import swgohgg_user
from scrapers import swgohgg_guild
from classes.usuarios import Usuario
from classes.gremio import Gremio
from classes.json import Json


def print_hi(name):
    print(f'Hola, {name}')


if __name__ == '__main__':
    print_hi('Casco Oscuro Bot')
    allycode = 167147967
    nombre_user = swgohgg_user.nombre_usuario()
    telegram_user = swgohgg_user.telegram_usuario()
    discord_user = swgohgg_user.discord_usuario()
    usuario = Usuario(nombre_user, allycode, telegram_user, discord_user)


url_guild = "https://swgoh.gg/g/708/discipulos-de-casco-oscuro/"
sopa_guild = swgohgg_guild.preparar_sopa(url_guild)
nombre_guild = swgohgg_guild.nombre_gremio(sopa_guild)
items_guild = swgohgg_guild.scrap_items_guild(sopa_guild)
miembros = swgohgg_guild.scrap_miembros_guild(sopa_guild)
print(miembros)
guild = Gremio(items_guild)
#crear_json = Json()
#miembros_json = crear_json.crear_json(miembros)
