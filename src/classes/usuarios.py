"""
Definición de las clases y los métodos de todo el programa
"""

class Usuario:
    def __init__(self, username, allycode, telegram, discord):
        self.username = username
        self.allycode = allycode
        self.telegram = telegram
        self.discord = discord
    
    def muestrausuario(self):
        print(self.username)
        print(self.allycode)
        if self.telegram == "":
            print("No dispone de Telegram")
        else:
            print(self.telegram)
        if self.discord =="":
            print("No dispone de Discord")
        else:
            print(self.discord)


