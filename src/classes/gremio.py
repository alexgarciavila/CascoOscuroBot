from unicodedata import name
from scrapers import swgohgg_guild
from classes.miembros import Miembros
import coreapi


class Gremio:
    def __init__(self, datos_guild):
        self.id = self.set_id(datos_guild)
        self.nombre = self.set_nombre(datos_guild)
        self.texto = self.set_texto_guild(datos_guild)
        self.banner_color_id = self.set_banner_color_id(datos_guild)
        self.banner_logo_id = self.set_banner_logo_id(datos_guild)
        self.enrollment_status = self.set_enrollment_status(datos_guild)
        self.galactic_power = self.set_galactic_power(datos_guild)
        self.avg_galactic_power = self.set_avg_galactic_power(datos_guild)
        self.guild_type = self.set_guild_type(datos_guild)
        self.level_requirement = self.set_level_requirement(datos_guild)
        self.member_count = self.set_member_count(datos_guild)
        self.avg_arena_rank = self.set_avg_arena_rank(datos_guild)
        self.avg_fleet_arena_rank = self.set_avg_fleet_arena_rank(datos_guild)
        self.avg_skill_rating = self.set_avg_skill_rating(datos_guild)
        self.last_sync = self.set_last_sync(datos_guild)


    def set_id(self, datos_guild):
        id = datos_guild["guild_id"]

        return id

    def set_nombre(self, datos_guild):
        nombre = datos_guild["name"]

        return nombre

    def set_texto_guild(self, datos_guild):
        texto = datos_guild["external_message"]

        return texto

    def set_banner_color_id(self, datos_guild):
        banner_color_id = datos_guild["banner_color_id"]

        return banner_color_id

    def set_banner_logo_id(self, datos_guild):
        banner_logo_id = datos_guild["banner_logo_id"]

        return banner_logo_id
    
    def set_enrollment_status(self, datos_guild):
        enrollment_status = datos_guild["enrollment_status"]

        return enrollment_status

    def set_galactic_power(self, datos_guild):
        galactic_power = datos_guild["galactic_power"]

        return galactic_power

    def set_avg_galactic_power(self, datos_guild):
        avg_galactic_power = datos_guild["avg_galactic_power"]

        return avg_galactic_power

    def set_guild_type(self, datos_guild):
        guild_type = datos_guild["guild_type"]

        return guild_type

    def set_level_requirement(self, datos_guild):
        level_requirement = datos_guild["level_requirement"]

        return level_requirement

    def set_member_count(self, datos_guild):
        member_count = datos_guild["member_count"]

        return member_count

    def set_avg_arena_rank(self, datos_guild):
        avg_arena_rank = datos_guild["avg_arena_rank"]

        return avg_arena_rank

    def set_avg_fleet_arena_rank(self, datos_guild):
        avg_fleet_arena_rank = datos_guild["avg_fleet_arena_rank"]

        return avg_fleet_arena_rank

    def set_avg_skill_rating(self, datos_guild):
        avg_skill_rating = datos_guild["avg_skill_rating"]

        return avg_skill_rating

    def set_last_sync(self, datos_guild):
        last_sync = datos_guild["last_sync"]

        return last_sync


    def listar_miembro(self, sopa_guild):
        """
        Listamos todos los miembros del gremio
        Tenemos que pasarle la sopa como parámetros
        """

        miembros = swgohgg_guild.scrap_miembros_guild(sopa_guild)
        for m in miembros.keys():
            items = miembros[m]
            members = Miembros(m, items)
            txt = ("El usuario {nombre} tiene un GP de {gp} "
                   "con un Skill Rating de {sk}. Su rango de "
                   "arena es {ar} y en naves {far}. "
                   "Su rol dentro del gremio es {role} y su URL "
                   "de swgoh es {url}"
                   ).format(
                            nombre=members.name,
                            gp=members.gp,
                            sk=members.playerskillrating,
                            ar=members.arenarank,
                            far=members.fleetarenarank,
                            role=members.role,
                            url=members.url
                            )
            print(txt)

    def buscar_miembro(self):
        print("hola")
