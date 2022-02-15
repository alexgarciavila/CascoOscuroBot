from scrapers import swgohgg_guild
from classes.miembros import Miembros


class Gremio:
    def __init__(self, items):
        self.gp = items["Galactic Power"]
        self.avggp = items["Avg Galactic Power"]
        self.rey = items["Rey"]
        self.slkr = items["SLKR"]
        self.jml = items["JML"]
        self.see = items["SEE"]
        self.jmk = items["JMK"]
        self.lv = items["LV"]
        self.chargp = items["Character GP"]
        self.shipgp = items["Ship GP"]
        self.avgsr = items["Avg Skill Rating"]
        self.avgarenarank = items["Avg Current Arena Rank"]
        self.avgshiparenarank = items["Avg Current Fleet Arena Rank"]

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
