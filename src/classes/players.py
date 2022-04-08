import coreapi
import json
from datetime import datetime


class Players:
    def __init__(self, allycode):
        self.ally_code = allycode
        self.player_api = ""
        self.player_data = ""
        self.player_units = ""
        self.has_reylg = False
        self.has_slkr = False
        self.has_jml = False
        self.has_see = False
        self.has_jmk = False
        self.has_lv = False
        # Extraidos de la API
        self.arena_leader_base_id = ""
        self.arena_rank = ""
        self.level = ""
        self.name = ""
        self.last_updated = ""
        self.galactic_power = ""
        self.character_gp = ""
        self.ship_gp = ""
        self.ship_battles_won = ""
        self.arena_battles_won = ""
        self.pve_battles_won = ""
        self.pve_hard_won = ""
        self.galactic_war_won = ""
        self.guild_raid_won = ""
        self.guild_contribution = ""
        self.guild_donations = ""
        self.season_full_clears = ""
        self.season_successful_defends = ""
        self.season_league_score = ""
        self.season_undersized_squad_wins = ""
        self.season_promotions_earned = ""
        self.season_banners_earned = ""
        self.season_offensive_battles_won = ""
        self.season_territories_defeated = ""
        self.url = ""
        self.arena = ""
        self.fleet_arena = ""
        self.skill_rating = ""
        self.division_number = ""
        self.league_name = ""
        self.league_frame_image = ""
        self.league_blank_image = ""
        self.league_image = ""
        self.division_image = ""
        self.portrait_image = ""
        self.title = ""
        self.guild_id = ""
        self.guild_name = ""
        self.guild_url = ""
        self.reylg_relic = ""
        self.slkr_relic = ""
        self.jml_relic = ""
        self.see_relic = ""
        self.jmk_relic = ""
        self.lv_relic = ""

    def search_player_api(self):
        """
        Conectamos con la API del jugador a través
        de su código de aliado
        """
        # Inicializamos el cliente que se conecta con la API
        client = coreapi.Client()
        # Importamos la estuctura de la api de un usuario
        self.player_api = client.get(f"https://swgoh.gg/api/player/"
                                     f"{self.ally_code}/")

    def search_player_data(self):
        """
        Recibimos los datos de la API del jugador
        y extraemos los correspondientes a
        su información.
        """
        self.player_data = self.player_api["data"]

    def search_player_units(self):
        """
        Recibimos los datos de la API del jugador
        y extraemos los correspondientes a las
        unidades que posee
        """
        self.player_units = self.player_api["units"]

    def set_player_data(self):
        """
        Función para setear los datos del jugador en función
        de su código de aliado
        """
        self.name = self.player_data["name"]
        self.arena_leader_base_id = self.player_data["arena_leader_base_id"]
        self.arena_rank = self.player_data["arena_rank"]
        self.level = self.player_data["level"]
        self.name = self.player_data["name"]
        self.last_updated = self.player_data["last_updated"]
        self.galactic_power = self.player_data["galactic_power"]
        self.character_gp = self.player_data["character_galactic_power"]
        self.ship_gp = self.player_data["ship_galactic_power"]
        self.ship_battles_won = self.player_data["ship_battles_won"]
        self.pvp_battles_won = self.player_data["pvp_battles_won"]
        self.pve_battles_won = self.player_data["pve_battles_won"]
        self.pve_hard_won = self.player_data["pve_hard_won"]
        self.galactic_war_won = self.player_data["galactic_war_won"]
        self.guild_raid_won = self.player_data["guild_raid_won"]
        self.guild_contribution = self.player_data["guild_contribution"]
        self.guild_donations = self.player_data["guild_exchange_donations"]
        self.season_full_clears = self.player_data["season_full_clears"]
        self.season_successful_defends = self.player_data[
            "season_successful_defends"
            ]
        self.season_league_score = self.player_data["season_league_score"]
        self.season_undersized_squad_wins = self.player_data[
            "season_undersized_squad_wins"
            ]
        self.season_promotions_earned = self.player_data["season_promotions_earned"]
        self.season_banners_earned = self.player_data["season_banners_earned"]
        self.season_offensive_battles_won = self.player_data[
            "season_offensive_battles_won"
            ]
        self.season_territories_defeated = self.player_data[
            "season_territories_defeated"
            ]
        self.url = self.player_data["url"]
        self.arena = self.player_data["arena"]
        self.fleet_arena = self.player_data["fleet_arena"]
        self.skill_rating = self.player_data["skill_rating"]
        self.division_number = self.player_data["division_number"]
        self.league_name = self.player_data["league_name"]
        self.league_frame_image = self.player_data["league_frame_image"]
        self.league_blank_image = self.player_data["league_blank_image"]
        self.league_image = self.player_data["league_image"]
        self.division_image = self.player_data["division_image"]
        self.portrait_image = self.player_data["portrait_image"]
        self.title = self.player_data["title"]
        self.guild_id = self.player_data["guild_id"]
        self.guild_name = self.player_data["guild_name"]
        self.guild_url = self.player_data["guild_url"]

    def player_loader(self):
        """
        Cargamos los datos locales.
        Si no existen, los actualizamos
        """

        in_file = f"json/{self.ally_code}_data.json"
        try:
            with open(in_file) as playerfile:
                self.player_api = json.load(playerfile)
        except FileNotFoundError:
            self.player_updater()
        # self.search_guild_data()
        # self.search_guild_members()
        # self.set_guild_data()

    def player_updater(self):
        """
        Actualizamos los datos del jugador y
        y los guardamos en un archivo Json
        """
        
        # Comprobamos si tenemos datos actualizados
        in_file = f"json/{self.ally_code}_data.json"
        try:
            with open(in_file) as playerfile:
                self.guild_api = json.load(playerfile)
                self.search_player_data()
                last_sync = datetime.strptime(self.player_data["last_updated"],"%Y-%m-%dT%H:%M:%S.%f")
                last_sync_date = last_sync.strftime("%d-%m-%Y")
                print(f"Los datos están actualizados a fecha "
                      f"de: {last_sync_date}\n")
                last_sync_today = datetime.today().strftime("%d-%m-%Y")
                if last_sync_date != last_sync_today:
                    print("¿Desea actualizar los datos? (S/N)")
                    answer = input(">>> ")
                    while True:
                        if answer.lower() == "s":
                            self.search_player_api()
                            self.search_player_data()
                            player_id = self.player_data["ally_code"]
                            out_file = f"json/{player_id}_data.json"
                            with open(out_file, "w") as playerfile:
                                json.dump(self.player_api, playerfile, indent=4)
                            break
                        elif answer.lower() == "n":
                            print("\nNo se han actualizados los datos.")
                            print(f"Última fecha de actualizacion: {last_sync_date}\n")
                            break
                        else:
                            print("Por favor, introduce S o N")
                            answer = input(">>> ")
                else:
                    print("Los datos ya están actualizados")
        except FileNotFoundError:
            print("Datos no encontrados...")
            print("Procedemos a actualizarlos")
            # Llamamos a la API para recolectar los datos del jugador
            self.search_player_api()
            self.search_player_data()
            # Eliminamos espacios para evitar errores en los ficheros
            player_id = self.player_data["ally_code"]
            # Grabamos los datos en un archivo Json
            out_file = f"json/{player_id}_data.json"
            with open(out_file, "w") as playerfile:
                json.dump(self.player_api, playerfile, indent=4)
        
        # member_name = miembro01.name.replace(" ", "_")

    def search_rey_lg(self):
        """
        Buscamos si tiene a REY LG.
        Devolvemos el nivel de Reliquia.
        """
        for unit in self.player_units:
            if unit["data"]["name"] == "Rey":
                self.has_reylg = True
                # La API da dos niveles de reliquia por encima
                self.reylg_relic = unit["data"]["relic_tier"] - 2
                break

    def search_slkr(self):
        """
        Buscamos si tiene a SLKR.
        Devolvemos el nivel de Reliquia.
        """
        for unit in self.player_units:
            if unit["data"]["name"] == "Supreme Leader Kylo Ren":
                self.has_slkr = True
                # La API da dos niveles de reliquia por encima
                self.slkr_relic = unit["data"]["relic_tier"] - 2
                break

    def search_jml(self):
        """
        Buscamos si tiene a JML.
        Devolvemos el nivel de Reliquia.
        """
        for unit in self.player_units:
            if unit["data"]["name"] == "Jedi Master Luke":
                self.has_jml = True
                # La API da dos niveles de reliquia por encima
                self.jml_relic = unit["data"]["relic_tier"] - 2
                break

    def search_see(self):
        """
        Buscamos si tiene a SEE.
        Devolvemos el nivel de Reliquia.
        """
        for unit in self.player_units:
            if unit["data"]["name"] == "Sith Eternal Emperor":
                self.has_see = True
                # La API da dos niveles de reliquia por encima
                self.see_relic = unit["data"]["relic_tier"] - 2
                break

    def search_jmk(self):
        """
        Buscamos si tiene a JMK.
        Devolvemos el nivel de Reliquia.
        """
        for unit in self.player_units:
            if unit["data"]["name"] == "Jedi Master Kenobi":
                self.has_jmk = True
                # La API da dos niveles de reliquia por encima
                self.jmk_relic = unit["data"]["relic_tier"] - 2
                break

    def search_lv(self):
        """
        Buscamos si tiene a LV.
        Devolvemos el nivel de Reliquia.
        """
        for unit in self.player_units:
            if unit["data"]["name"] == "Lord Vader":
                self.has_lv = True
                # La API da dos niveles de reliquia por encima
                self.lv_relic = unit["data"]["relic_tier"] - 2
                break
