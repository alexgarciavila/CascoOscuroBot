import coreapi
import json
from datetime import datetime
from classes.members import Members


class Guild:
    def __init__(self, guild_id):
        self.id = guild_id
        self.guild_api = ""
        self.guild_data = ""
        self.guild_members = ""
        # Extraidos de la API
        self.name = ""
        self.text = ""
        self.banner_color_id = ""
        self.banner_logo_id = ""
        self.enrollment_status = ""
        self.galactic_power = ""
        self.avg_galactic_power = ""
        self.guild_type = ""
        self.level_requirement = ""
        self.member_count = ""
        self.avg_arena_rank = ""
        self.avg_fleet_arena_rank = ""
        self.avg_skill_rating = ""
        self.last_sync = ""

    def search_guild_api(self):
        """
        Conectamos con la API de la guild a través
        de su id
        """
        # Inicializamos el cliente que se conecta con la API
        client = coreapi.Client()
        # Importamos la estuctura de la api de un usuario
        self.guild_api = client.get(f"https://swgoh.gg/api/guild-profile/"
                               f"{self.id}/")

    def search_guild_data(self):
        """
        Recibimos los datos de la API de la guild
        y extraemos los correspondientes a
        su información
        """
        self.guild_data = self.guild_api["data"]
    
    def search_guild_members(self):
        self.guild_members = self.guild_data["members"]
    
    def set_guild_data(self):
        """
        Función para setear los datos de la guild en
        función del id de la guild
        """
        self.id = self.guild_data["guild_id"]
        self.name = self.guild_data["name"]
        self.text = self.guild_data["external_message"]
        self.banner_color_id = self.guild_data["banner_color_id"]
        self.banner_logo_id = self.guild_data["banner_logo_id"]
        self.enrollment_status = self.guild_data["enrollment_status"]
        self.galactic_power = self.guild_data["galactic_power"]
        self.avg_galactic_power = self.guild_data["avg_galactic_power"]
        self.guild_type = self.guild_data["guild_type"]
        self.level_requirement = self.guild_data["level_requirement"]
        self.member_count = self.guild_data["member_count"]
        self.avg_arena_rank = self.guild_data["avg_arena_rank"]
        self.avg_fleet_arena_rank = self.guild_data["avg_fleet_arena_rank"]
        self.avg_skill_rating = self.guild_data["avg_skill_rating"]
        self.last_sync = self.guild_data["last_sync"]

    def list_members(self):
        """
        Listamos todos los miembros del gremio
        """
        for index, guild_member in enumerate(self.guild_members):
            ally_code = guild_member["ally_code"]
            member = Members(ally_code)
            member.search_player_api()
            member.search_player_data()
            member.set_player_data()
            member.role = guild_member["member_level"]
            name = member.name
            gp = member.galactic_power
            sk = member.skill_rating
            ar = member.arena["rank"]
            far = member.fleet_arena["rank"]
            role = self.role_member(member.role)
            antiguedad = guild_member["guild_join_time"]
            url = f"https://swgoh.gg/p/{ally_code}/"
            txt = (f"\n################################################"
                   f"\nMiembro {index+1} - {name}"
                   f"\n################################################"
                   f"\n# GP: {gp} "
                   f"\n# Skill Rating: {sk}"
                   f"\n# Rango de arena: {ar}"
                   f"\n# Rango de naves {far}"
                   f"\n# Rol dentro del gremio: {role}"
                   f"\n# URL de swgoh.gg: {url}"
                   f"\n# Se unió al gremio el {antiguedad}"
                   f"\n################################################"
                   )
            print(txt)

    def role_member(self, member_level):
        """
        Asignamos un rol en base al nivel numérico
        que nos devuelve la API
        """
        if member_level == 4:
            rol = "Lidl"
        elif member_level == 3:
            rol = "Oficial"
        else:
            rol = "Miembro"
        return rol

    def guild_updater(self):
        """
        Actualizamos los datos de la guild y
        y los guardamos en un archivo Json
        """
        
        # Comprobamos si tenemos datos actualizados
        in_file = f"json/{self.id}_data.json"
        with open(in_file) as guildfile:
            self.guild_api = json.load(guildfile)
            self.search_guild_data()
        
        last_sync = datetime.strptime(self.guild_data["last_sync"],"%Y-%m-%dT%H:%M:%S.%f")
        last_sync_date = last_sync.strftime("%d-%m-%Y")
        print(f"Los datos están actualizados a fecha "
              f"de: {last_sync_date}\n")
        last_sync_today = datetime.today().strftime("%d-%m-%Y")
        if last_sync_date != last_sync_today:
            print("¿Desea actualizar los datos?")
        else:
            print("Los datos ya están actualizados")
        
        #member_name = miembro01.name.replace(" ", "_")
        # Llamamos a la API para recolectar los datos de la guild
        self.search_guild_api()
        self.search_guild_data()
        guild_name = self.guild_data["guild_id"].replace(" ", "_")
        #out_file = f"json/{member_name}_data.json"
        #with open(out_file, "w") as memberfile:
        #    json.dump(miembro01.player_data, memberfile, indent=4)


        #out_file = f"json/{member_name}_units.json"
        #with open(out_file, "w") as memberfile:
        #    json.dump(player01.player_units, memberfile, indent=4)

        out_file = f"json/{guild_name}_data.json"
        with open(out_file, "w") as guildfile:
            json.dump(self.guild_api, guildfile, indent=4)