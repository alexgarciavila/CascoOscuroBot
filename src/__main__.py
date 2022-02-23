from scrapers import swgohgg_user
from scrapers import swgohgg_guild
from classes.usuarios import Usuario
from classes.gremio import Gremio
from classes.miembros import Miembros
from classes.json import Json
import coreapi
from bots import telegrambot


def print_hi(name):
    print(f'Hola, {name}')


if __name__ == '__main__':
    print_hi('Casco Oscuro Bot')
    allycode = 167147967
    nombre_user = swgohgg_user.nombre_usuario()
    telegram_user = swgohgg_user.telegram_usuario()
    discord_user = swgohgg_user.discord_usuario()
    usuario = Usuario(nombre_user, allycode, telegram_user, discord_user)


#url_guild = "https://swgoh.gg/g/708/discipulos-de-casco-oscuro/"
#sopa_guild = swgohgg_guild.preparar_sopa(url_guild)

#url_guild2 = "https://swgoh.gg/g/oAYG8MpVSfigDgyI75C-qQ/"
#sopa_guild2 = swgohgg_guild.preparar_sopa(url_guild2)

#nombre_guild = swgohgg_guild.nombre_gremio(sopa_guild)
#items_guild = swgohgg_guild.scrap_items_guild(sopa_guild)
# miembros = swgohgg_guild.scrap_miembros_guild(sopa_guild)
# print(miembros)
#guild = Gremio(items_guild)


#nombre_guild2 = swgohgg_guild.nombre_gremio(sopa_guild2)
#items_guild2 = swgohgg_guild.scrap_items_guild(sopa_guild2)
#guild2 = Gremio(items_guild2)

#guild.listar_miembro(sopa_guild)

#swgohgg_guild.comparar_gremio(guild, guild2, nombre_guild, nombre_guild2)


# Initialize a client & load the schema document
client = coreapi.Client()
schema = client.get("https://swgoh.gg/api/guild-profile/0JadhFYYRxa42RChGLFxvA/")
datos = schema["data"]
miembros = datos["members"]

"""
print(datos.keys())
-------------------
odict_keys(['guild_id', 'name', 'external_message', 'banner_color_id',
'banner_logo_id', 'enrollment_status', 'galactic_power', 'guild_type',
'level_requirement', 'member_count', 'members', 'avg_galactic_power',
'avg_arena_rank', 'avg_fleet_arena_rank', 'avg_skill_rating', 'last_sync'])
"""


"""
print(miembros[1].keys())
-------------------------
odict_keys(['galactic_power', 'guild_join_time', 'lifetime_season_score',
'member_level', 'ally_code', 'player_level', 'player_name', 'league_id',
'league_name', 'league_frame_image', 'portrait_image', 'title', 'squad_power'])

"""
"""
Ejemplo
print(schema["data"]["members"][1]["player_name"])
"""
"""for m in miembros:
    print(m["player_name"])
"""

id_gremio = "0JadhFYYRxa42RChGLFxvA"
cascos = Gremio(datos)
print(cascos.id)
print(cascos.nombre)
print(cascos.texto)
print(cascos.banner_color_id)
print(cascos.banner_logo_id)
print(cascos.enrollment_status)
print(cascos.galactic_power)
print(cascos.avg_galactic_power)
print(cascos.guild_type)
print(cascos.level_requirement)
print(cascos.member_count)
print(cascos.avg_arena_rank)
print(cascos.avg_fleet_arena_rank)
print(cascos.avg_skill_rating)
print(cascos.last_sync)

#telegrambot.main()
