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
            print(members.name)
            print(members.url)
            print(members.gp)
            print(members.playerskillrating)
            print(members.arenarank)
            print(members.fleetarenarank)
            print(members.role)
