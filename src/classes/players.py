import coreapi


class Players:
    def __init__(self, allycode):
        self.ally_code = allycode
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

    def search_player(self):
        """
        Conectamos con la API del jugador a través
        de su código de aliado
        """
        # Inicializamos el cliente que se conecta con la API
        client = coreapi.Client()
        # Importamos la estuctura de la api de un usuario
        player_api = client.get(f"https://swgoh.gg/api/player/{self.ally_code}/")
        player_data = self.search_player_data(player_api)
        self.set_player_data(player_data)
        player_units = self.search_player_units(player_api)
        # print(player_data)
        # print(player_units)

    def search_player_data(self, player_api):
        """
        Recibimos los datos de la API del jugador
        y extraemos los correspondientes a
        su información
        """
        player_data = player_api["data"]

        return player_data

    def search_player_units(self, player_api):
        """
        Recibimos los datos de la API del jugador
        y extraemos los correspondientes a las
        unidades que posee
        """
        player_units = player_api["units"]

        return player_units

    def set_player_data(self, player_data):
        """
        Función para setear los datos del jugador en función
        de su código de aliado
        """
        self.name = player_data["name"]
        self.arena_leader_base_id = player_data["arena_leader_base_id"]
        self.arena_rank = player_data["arena_rank"]
        self.level = player_data["level"]
        self.name = player_data["name"]
        self.last_updated = player_data["last_updated"]
        self.galactic_power = player_data["galactic_power"]
        self.character_gp = player_data["character_galactic_power"]
        self.ship_gp = player_data["ship_galactic_power"]
        self.ship_battles_won = player_data["ship_battles_won"]
        self.pvp_battles_won = player_data["pvp_battles_won"]
        self.pve_battles_won = player_data["pve_battles_won"]
        self.pve_hard_won = player_data["pve_hard_won"]
        self.galactic_war_won = player_data["galactic_war_won"]
        self.guild_raid_won = player_data["guild_raid_won"]
        self.guild_contribution = player_data["guild_contribution"]
        self.guild_donations = player_data["guild_exchange_donations"]
        self.season_full_clears = player_data["season_full_clears"]
        self.season_successful_defends = player_data[
            "season_successful_defends"
            ]
        self.season_league_score = player_data["season_league_score"]
        self.season_undersized_squad_wins = player_data[
            "season_undersized_squad_wins"
            ]
        self.season_promotions_earned = player_data["season_promotions_earned"]
        self.season_banners_earned = player_data["season_banners_earned"]
        self.season_offensive_battles_won = player_data[
            "season_offensive_battles_won"
            ]
        self.season_territories_defeated = player_data[
            "season_territories_defeated"
            ]
        self.url = player_data["url"]
        self.arena = player_data["arena"]
        self.fleet_arena = player_data["fleet_arena"]
        self.skill_rating = player_data["skill_rating"]
        self.division_number = player_data["division_number"]
        self.league_name = player_data["league_name"]
        self.league_frame_image = player_data["league_frame_image"]
        self.league_blank_image = player_data["league_blank_image"]
        self.league_image = player_data["league_image"]
        self.division_image = player_data["division_image"]
        self.portrait_image = player_data["portrait_image"]
        self.title = player_data["title"]
        self.guild_id = player_data["guild_id"]
        self.guild_name = player_data["guild_name"]
        self.guild_url = player_data["guild_url"]
