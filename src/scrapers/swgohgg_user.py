﻿import requests
from bs4 import BeautifulSoup as bs
import re

r = requests.get("https://swgoh.gg/p/167147967/", timeout=5)
soup = bs(r.text, "html.parser")


def nombre_usuario():
    """ Función para scrapear el nombre de un usuario """
    find_nombre = soup.find("h5", class_="panel-title text-center")
    nombre = find_nombre.get_text()
    return nombre


def telegram_usuario():
    """ Función para scrapear el usuario de Telegram de un usuario """
    find_telegram = soup.find("strong", class_="pull-right", text=re.compile(r"@"))
    telegram = find_telegram.get_text()
    return telegram


def discord_usuario():
    """ Función para scrapear el usuario de Discord de un usuario """

    find_discord = soup.find("h5", class_="panel-title text-center")
    discord = find_discord.get_text()
    return discord
