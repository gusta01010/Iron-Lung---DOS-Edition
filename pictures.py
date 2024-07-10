import time
import sys
import pygame

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None) #Inicializa o som do pygame
def picture1():
    ocean_floor = """
            .  .        ~      .    .     ~
        .                .         ~
            ~        .                 .
    .   ~       .                ~
            .           ~     .        ~
    ___    .    ____     .     ___   .   __
    (   )      _(    )_.--.____(   )_____(_))
    | |______/     .'    \     `-'    \   ` \\
    |         `.  /  _.-' \ `.   .'`.  \  `. \\
    |    _.-'  )/  /      )|  `-'    \  \   \|
    |_.-'  .-' /.-'   .   (/  .-.     `. \\
        _.-'   (     ('    )   |   )     ) \\
    /        \  ( \    /|   '-'     .'  \\
    /     .    \  '.'-       ,     .'    /
    /   .'      '. |      ,  |    /    .'/
    /   /  .  .-'  '|    _/|   | .-'_.-' /
    \  (    \/      \ .-' |   | \  '   .'
    \  \    \       '.   `--'   \    /
    '. '.   \        \__________'-.'
        '._)  .'      ___\_____)___>
            (___.-""'          `"
    """
    print(ocean_floor)


def picture2():
    letter = """Isso não se trata de uma expedição. É uma execução. Quando te colocam aqui,
não querem que você volte. E mesmo que você cumpra, e mesmo que eles cumpr-
am suas promessas... Que liberdade espera por você? Alguns navios naufrágos
em um mar de estrelas mortas?

Se ainda há esperança, ela está além do véu. A esperança neste vazio  é tão
ilusória quanto a luz das estrelas. Escolherei meu último respiro no  fundo
de um oceano, invisível, inouvido e descontrolado.

Eles serão executados.

Ainda conseguirei a minha liberdade.

    """
    ocean_crystal = """
            ~         .  .    ~    .   ~
        .        ~        .       ~
    ~       .     ~        .        ~
        .  ~           .  ~       .
    ~        .    ~      .   ~      .
        ~        ____     ~     ~
    .     ____.'/    \     .     ~
        ___/.-. '/      \___   .   ~
    __/ __   \/    /\   \  \___
    (    \_\_____/ /\ \   \___  '.
    \      __`-_.'  \ \      /  /
    \    /  \       \ \    /__/
    \  /   /`.      \ \__/  /
    ___\/___/   \______\__/  /
    /   |   \     /     |    /
    \   |    \   /      |___/
    \  |     \ /      /   /
    \ |      V      /   /
    \|             /  /
        \            /  /
        \          /  /
        \________/  /
        \        /
            \______/
    """
    print(ocean_crystal)
    time.sleep(3)
    print("\nDurante a fotografia, você percebe que uma carta cai de cima do monitor")
    time.sleep(0.5)
    print("\n.", end='', flush=True) #End='' nao cria uma nova linha abaixo
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1.5)
    print(".")
    time.sleep(2)
    print("Eu pego a carta e leio")
    time.sleep(2)
    print("---------------------------------------------------------------------------")
    for char in letter: #Imprime as letras aos poucos
        sys.stdout.write(char) #Escreve o caractere
        sys.stdout.flush() #Vai atualizando e forçando a mostrar os caracteres
        time.sleep(0.065) #Tempo de espera até o novo caractere escrever

class SomPlay:
    def __init__(self):
        self.notplayed = True
    def picture3(self):
        horrifying_creature = """
        ╔═════════════════════════════════════╗
        ║                                     ║
        ║         ◦◦    ◦◦    ◦◦    ◦◦        ║
        ║       ◦◦  ◦◦◦◦  ◦◦◦◦  ◦◦◦◦  ◦◦      ║
        ║     ◦◦                        ◦◦    ║
        ║   ◦◦    ▒▒            ▒▒        ◦◦  ║
        ║ ◦◦      ▒▒            ▒▒          ◦◦║
        ║◦       ▒▒▒▒          ▒▒▒▒          ◦║
        ║        ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓           ║
        ║       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ║
        ║      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ║
        ║     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ║
        ║ ┌──▓▓▓▓▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▓▓▓──┐   ║
        ║ │▓▓▓▓▀   ▄▄▄▄▄        ▄▄▄▄   ▀▓▓▓│  ║
        ║ │▓▓▀    █████▀        ▀█████   ▀▓│  ║
        ║ │▓▀    ██████          ██████   ▀│  ║
        ║ │     ███████          ███████    │ ║
        ║ │    ████████▄        ▄████████   │ ║
        ║ │    ████████████████████████████ │ ║
        ║ │    ████████████████████████████ │ ║
        ║ │     ██████████████████████████  │ ║
        ║ │      ████████████████████████   │ ║
        ║ │       ██████████████████████    │ ║
        ║ │         ████████████████████    │ ║
        ║ │           ████████████████      │ ║
        ║ └─────────────────────────────────┘ ║
        ╚═════════════════════════════════════╝
        """
        print(horrifying_creature)
        if  self.notplayed == True:
            bloop = pygame.mixer.Sound('sounds/sfx/bloop.mp3')
            bloop.play()
            self.notplayed = False


def picture4():
    snake_eye = """
    ╔═════════════════════════════════╗
    ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
    ║░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░║
    ║░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░░║
    ║░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░║
    ║░░▒▒▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▒▒░░░░░║
    ║░▒▒▓▓▓▓▓▓██████████████▓▓▓▓▒▒░░░░║
    ║░▒▓▓▓▓▓▓████████████████▓▓▓▓▒░░░░║
    ║▒▒▓▓▓▓██████████████████▓▓▓▓▒▒░░░║
    ║▒▓▓▓▓████████■■■■████████▓▓▓▓▒░░░║
    ║▒▓▓▓████████■    ■████████▓▓▓▒░░░║
    ║▒▓▓▓████████■    ■████████▓▓▓▒░░░║
    ║░▒▓▓▓██████████■■████████▓▓▓▒░░░░║
    ║░▒▒▓▓▓████████████████▓▓▓▓▒░░░░░░║
    ║░░▒▒▓▓▓▓██████████▓▓▓▓▓▓▒▒░░░░░░░║
    ║░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░║
    ║░░░░░▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒░░░░░░░░░░░░║
    ║░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░║
    ╚═════════════════════════════════╝
    """
    print(snake_eye)
    
    time.sleep(1.7)
    loadpoint = "..."
    growl = pygame.mixer.Sound('sounds/sfx/growl.mp3')
    growl.play()
    print("De repente, sua visão começa a embaçar...\n")
    for load in loadpoint: #Carrega lentamente os 3 pontos
        time.sleep(2.9)
        print(".", end='')
    time.sleep(1)
    sys.exit(1)
