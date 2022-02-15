class Miembros:
    def __init__(self, nombre, items):
        self.name = nombre
        self.url = items["URL"]
        self.gp = items["GP"]
        self.playerskillrating = items["Player Skill Rating"]
        self.arenarank = items["Arena Rank"]
        self.fleetarenarank = items["Fleet Arena Rank"]
        self.role = items["Role"]
