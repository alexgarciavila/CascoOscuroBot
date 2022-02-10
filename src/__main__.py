from scrapers import swgohgg_user
from scrapers import swgohgg_guild
from classes.usuarios import Usuario
from classes.gremio import Gremio

def print_hi(name):
    print(f'Hola, {name}')


if __name__ == '__main__':
    print_hi('Casco Oscuro Bot')
    allycode = 167147967
    nombre_user = swgohgg_user.nombre_usuario()
    telegram_user = swgohgg_user.telegram_usuario()
    discord_user = swgohgg_user.discord_usuario()
    usuario = Usuario(nombre_user,allycode,telegram_user,discord_user)
    #print("Usuario: ",usuario.username)
    #print("Código de aliado: ",usuario.allycode)
    #print("Usuario de Telegram: ",usuario.telegram)
    #print("Usuario de Discord: ",usuario.discord)


url_guild = "https://swgoh.gg/g/708/discipulos-de-casco-oscuro/"
sopa_guild = swgohgg_guild.preparar_sopa(url_guild)
nombre_guild = swgohgg_guild.nombre_gremio(sopa_guild)
#sopa_guild = swgohgg_guild.preparar_sopa(url_guild) # Revisar
#activos_swgohgg = swgohgg_guild.activos(sopa_guild)
#print(activos_swgohgg)
items_guild = swgohgg_guild.scrap_items_guild(sopa_guild)
miembros = swgohgg_guild.scrap_miembros_guild(sopa_guild)
guild = Gremio(items_guild)


