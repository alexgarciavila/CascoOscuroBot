from src.scrapers import swgohgg
from src.classes.usuarios import Usuario


def print_hi(name):
    print(f'Hola, {name}')


if __name__ == '__main__':
    print_hi('Casco Oscuro Bot')
    allycode = 167147967
    nombreuser = swgohgg.nombreusuario()
    telegramuser = swgohgg.telegramusuario()
    discorduser = swgohgg.discordusuario()
    usuario = Usuario(nombreuser,allycode,telegramuser,discorduser)
    print("Usuario: ",usuario.username)
    print("Código de aliado: ",usuario.allycode)
    print("Usuario de Telegram: ",usuario.telegram)
    print("Usuario de Discord: ",usuario.discord)


