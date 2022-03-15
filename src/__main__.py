from scrapers import swgohgg_user
from scrapers import swgohgg_guild
from classes.usuarios import Usuario
from classes.gremio import Gremio
from classes.miembros import Miembros
from classes.players import Players
from classes.json import Json
import coreapi
from bots import telegrambot


def print_hi(name):
    print(f'Hola, {name}')


if __name__ == '__main__':
    print_hi('Casco Oscuro Bot')
    


# url_guild = "https://swgoh.gg/g/708/discipulos-de-casco-oscuro/"
# sopa_guild = swgohgg_guild.preparar_sopa(url_guild)

# url_guild2 = "https://swgoh.gg/g/oAYG8MpVSfigDgyI75C-qQ/"
# sopa_guild2 = swgohgg_guild.preparar_sopa(url_guild2)

# nombre_guild = swgohgg_guild.nombre_gremio(sopa_guild)
# items_guild = swgohgg_guild.scrap_items_guild(sopa_guild)
# miembros = swgohgg_guild.scrap_miembros_guild(sopa_guild)
# print(miembros)
# guild = Gremio(items_guild)


# nombre_guild2 = swgohgg_guild.nombre_gremio(sopa_guild2)
# items_guild2 = swgohgg_guild.scrap_items_guild(sopa_guild2)
# guild2 = Gremio(items_guild2)

# guild.listar_miembro(sopa_guild)

# swgohgg_guild.comparar_gremio(guild, guild2, nombre_guild, nombre_guild2)

"""
print(datos_g1.keys())
-------------------
odict_keys(['guild_id', 'name', 'external_message', 'banner_color_id',
'banner_logo_id', 'enrollment_status', 'galactic_power', 'guild_type',
'level_requirement', 'member_count', 'members', 'avg_galactic_power',
'avg_arena_rank', 'avg_fleet_arena_rank', 'avg_skill_rating', 'last_sync'])
"""

# Extraemos en una lista cada miembros de la guild.
# Cada elemento de la lista contiene un diccionario con los datos
# de cada miembro de la guild
#miembros_g1 = datos_g1["members"]

"""
print(miembros_g1[1].keys())
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



#id_gremio = "0JadhFYYRxa42RChGLFxvA"
#cascos = Gremio("0JadhFYYRxa42RChGLFxvA")
#cascos.search_guild()
#cascos.listar_miembro(cascos.id)
#miembro1 = Miembros(miembros_g1)
#print(miembro1.name)

#telegrambot.main()

player01 = Players("336544232")
player01.search_player_api()
player01.search_player_data(player01.player_api)
player01.set_player_data(player01.player_data)
player01.search_player_units(player01.player_api)
print(player01.name)
print(player01.player_units)
