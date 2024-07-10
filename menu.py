#Classe Menu
import keyboard
import os
import time
import sys
import textwrap
import shutil
import pygame

def center_text(text, width=None): #Centraliza o texto da inicialização
    if width is None:
        width = shutil.get_terminal_size().columns #Pega o tamanho do terminal em sua coluna
    centered_lines = []
    for paragraph in text.split('\n\n'): #Utiliza a função textwrap
        lines = textwrap.wrap(paragraph, width=width)
        centered_lines.extend(line.center(width) for line in lines)
        centered_lines.append('') #Cria linha vazia para centralizar 
    return '\n'.join(centered_lines)

import random

def add_bubbles(circle, num_bubbles=5):
    RED = "\033[91m" #Cor da bolha O
    RESET = "\033[0m" #Termina a formatação
    lines = circle.split('\n')
    for _ in range(num_bubbles):
        bubble_line = random.randint(len(lines) // 5, len(lines) - 6) #divisao inteira == //
        bubble_col = random.randint(5, len(lines[bubble_line]) - 2)
        lines[bubble_line] = (
            lines[bubble_line][:bubble_col] +
            RED + 'O' + RESET + #Aplica a bolha
            lines[bubble_line][bubble_col+1:]
        )
    return '\n'.join(lines)

def animate_bubbles(circle, duration=37, frequency=0.9):
    start_time = time.time()
    while time.time() - start_time < duration:
        bubbled_circle = add_bubbles(circle)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(bubbled_circle)
        time.sleep(frequency)

def fill_circle(frequency):
    soundnew = 0
    hollow_circle = """
                    ,a@@@@@@@@@@@@@@a,
                ,@@@@@@@@@@@@@@@@@@@@@@,
            ,@@@@@@@@                @@@@@@,
            ,@@@@@@'                      '@@@@@@,
        ,@@@@@@'                          '@@@@@@,
        @@@@@@'                              '@@@@@@
    ,@@@@@'                                  '@@@@@,
    @@@@@@'                                    '@@@@@@
    @@@@@@                                        @@@@@@
    ,@@@@@                                          @@@@@,
    @@@@@@                                          @@@@@@
    @@@@@@                                          @@@@@@
    @@@@@@                                          @@@@@@
    @@@@@@                                          @@@@@@
    @@@@@@                                          @@@@@@
    '@@@@@,                                        ,@@@@@'
    @@@@@@                                        @@@@@@
    @@@@@@,                                    ,@@@@@@
    '@@@@@,                                  ,@@@@@'
        @@@@@@,                              ,@@@@@@
        '@@@@@@,                          ,@@@@@@'
            '@@@@@@,                      ,@@@@@@'
            '@@@@@@,                ,@@@@@@'
                '@@@@@@@@@@@@@@@@@@@@@@'
                    '@@@@@@@@@@@@@@'
    """


    # Anima as bolhas por 37 segundos, infelizmente quebrado caso duration altere
    animate_bubbles(hollow_circle, duration=37, frequency=0.05)

    # Preenche o círculo
    lines = hollow_circle.split('\n') #divisao do circulo em linhas
    filled_lines = lines.copy() 
    for i in range(len(lines) - 1, -1, -1): #Preenchimento até -1, passo de -1
        if '@' in lines[i]: #Se tiver @ na linha
            start = lines[i].index('@') #Arroba inicial
            end = lines[i].rindex('@') #Arroba final
            filled_part = lines[i][:start] + '█' * (end - start + 1) + lines[i][end+1:] #Preenche o círculo entre o final e o início
            filled_lines[i] = filled_part

            # Limpa a tela e imprime o círculo atualizado
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n'.join(filled_lines))

            time.sleep(0.02)  # Pausa controlada pela frequência
    
    time.sleep(24)
    if soundnew == 0: #Não é necessário, mas essa condição sempre fica true devido a variável ter sido declarada dentro do método, só comoaviso
        pygame.mixer.music.load('sounds/main/ambient.mp3')
        pygame.mixer.music.play(loops = -1)
        soundnew = 1
    

def beginning():
    introgame = ('\033[92m' + """
DÉCADAS ATRÁS, TODAS AS ESTRELAS CONHECIDAS E PLANETAS HABITÁVEIS DESAPARECERAM, DEIXANDO APENAS AQUELES QUE ESTAVAM EM ESTAÇÕES ESPACIAIS OU NAVES ESTELARES. ESSE EVENTO FICOU CONHECIDO COMO O ARREBATAMENTO SILENCIOSO.

COM OS SUPRIMENTOS DIMINUINDO E A INFRAESTRUTURA DESMORONANDO, OS SOBREVIVENTES AGORA ESTÃO A PROCURA DE QUALQUER VESTÍGIO DE RECURSOS NATURAIS EM UM UNIVERSO DE LUAS ESTÉREIS, ILUMINADO PELA LUZ FANTASMA DE ESTRELAS DESAPARECIDAS.

UMA DESSAS LUAS GUARDA UMA ESTRANHA ANOMALIA: UM OCEANO DE SANGUE. VOCÊ É UM CONDENADO, ENCARREGADO DE EXPLORAR ESSA ANOMALIA EM UM SUBMARINO IMPROVISADO, TENTANDO NAVEGAR APENAS COM FERRAMENTAS E INSTRUMENTOS QUE ESTÃO DISPONÍVEIS NO SUBMARINO APELIDADO DE IRON LUNG (PULMÃO DE FERRO). ELE NÃO FOI PROJETADO PARA ESSA PROFUNDIDADE, ENTÃO VOCÊ SERÁ SOLDADO DENTRO E A JANELA FRONTAL SERÁ FECHADA.

NÃO HOUVE TEMPO PARA TREINAMENTO.

SE FOR BEM-SUCEDIDO, VOCÊ GANHA A SUA LIBERDADE.""" + '\033[0m')
    centered_text = center_text(introgame.strip(), width=80)  # Ajuste a largura do texta da intro conforme necessário
    a = 0.05 #tempo para o caractere imprimir na tela
    for char in centered_text: #Loop para imprimir os caracteres, com base no texto centralizado
        print(char, end='', flush=True) #Flush força o caracere a aparecer e atualiza o buffer (pelo que entendi)
        if keyboard.is_pressed('enter'):
            time.sleep(0.005)
        else:
            time.sleep(a)
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')#Inicializa a introdução da descida do submarino
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
    pygame.mixer.music.stop()
    pygame.mixer.music.load('sounds/main/voice.mp3')
    pygame.mixer.music.play()
    fill_circle(0.045) #Inicializa a funcao de preencher o círculo, e o seu tempo de preenchimento

class Menu:
    def __init__(self):
        self.ym = 1
        self.ismenu = True
        self.RESET = "\033[0m"
        self.INVERSE = "\033[7m"
        os.system('mode con: cols=84 lines=29')
    def text(self):
        if keyboard.is_pressed('up') and self.ym != 1:
            self.ym -= 1
        if keyboard.is_pressed('down') and self.ym != 3:
            self.ym += 1

        if self.ym == 1:
            print(f"""            
    88 88""Yb  dP"Yb  88b 88     88     88   88 88b 88  dP""b8 
    88 88__dP dP   Yb 88Yb88     88     88   88 88Yb88 dP   `" 
    88 88"Yb  Yb   dP 88 Y88     88  .o Y8   8P 88 Y88 Yb  "88 
    88 88  Yb  YbodP  88  Y8     88ood8 `YbodP' 88  Y8  YboodP
                
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║                        {self.INVERSE}┌─────────────┐{self.RESET}                        ║
    ║                        {self.INVERSE}│  Novo Jogo  │{self.RESET}                        ║
    ║                        {self.INVERSE}└─────────────┘{self.RESET}                        ║
    ║                                                               ║
    ║                        ┌─────────────┐                        ║
    ║                        │  Controles  │                        ║
    ║                        └─────────────┘                        ║
    ║                                                               ║
    ║                        ┌─────────────┐                        ║
    ║                        │    Sair     │                        ║
    ║                        └─────────────┘     [↑] Subir          ║
    ║                                            [↓] Descer         ║
    ║                                            [ENTER] Selecionar ║
    ╚═══════════════════════════════════════════════════════════════╝
            """)
        if self.ym == 2:
            print(f"""            
    88 88""Yb  dP"Yb  88b 88     88     88   88 88b 88  dP""b8 
    88 88__dP dP   Yb 88Yb88     88     88   88 88Yb88 dP   `" 
    88 88"Yb  Yb   dP 88 Y88     88  .o Y8   8P 88 Y88 Yb  "88 
    88 88  Yb  YbodP  88  Y8     88ood8 `YbodP' 88  Y8  YboodP
                
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║                        ┌─────────────┐                        ║
    ║                        │  Novo Jogo  │                        ║
    ║                        └─────────────┘                        ║
    ║                                                               ║
    ║                        {self.INVERSE}┌─────────────┐{self.RESET}                        ║
    ║                        {self.INVERSE}│  Controles  │{self.RESET}                        ║
    ║                        {self.INVERSE}└─────────────┘{self.RESET}                        ║
    ║                                                               ║
    ║                        ┌─────────────┐                        ║
    ║                        │    Sair     │                        ║
    ║                        └─────────────┘     [↑] Subir          ║
    ║                                            [↓] Descer         ║
    ║                                            [ENTER] Selecionar ║               
    ╚═══════════════════════════════════════════════════════════════╝
            """)
        if self.ym == 3:
            print(f"""            
    88 88""Yb  dP"Yb  88b 88     88     88   88 88b 88  dP""b8 
    88 88__dP dP   Yb 88Yb88     88     88   88 88Yb88 dP   `" 
    88 88"Yb  Yb   dP 88 Y88     88  .o Y8   8P 88 Y88 Yb  "88 
    88 88  Yb  YbodP  88  Y8     88ood8 `YbodP' 88  Y8  YboodP
                
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║                        ┌─────────────┐                        ║
    ║                        │  Novo Jogo  │                        ║
    ║                        └─────────────┘                        ║
    ║                                                               ║
    ║                        ┌─────────────┐                        ║
    ║                        │  Controles  │                        ║
    ║                        └─────────────┘                        ║
    ║                                                               ║
    ║                        {self.INVERSE}┌─────────────┐{self.RESET}                        ║
    ║                        {self.INVERSE}│    Sair     │{self.RESET}                        ║
    ║                        {self.INVERSE}└─────────────┘{self.RESET}     [↑] Subir          ║
    ║                                            [↓] Descer         ║
    ║                                            [ENTER] Selecionar ║   
    ╚═══════════════════════════════════════════════════════════════╝
            """)
        time.sleep(0.050)
        os.system('cls||clear')



    def start(self):
        if keyboard.is_pressed('enter'):
            self.ismenu = False
            time.sleep(0.050)
            os.system('cls||clear')
            print("Starting Game...")
            time.sleep(2)
            os.system('cls||clear')
            beginning()
            os.system('cls||clear')
            return True
        return False
        

    def controls(self):
        if keyboard.is_pressed('enter'):
            self.ismenu = False
            time.sleep(0.050)
            os.system('cls||clear')
            print("""
+-----------------------------------+
|         CONTROLES DO JOGO         |
+-----------------------------------+
|                                   |
|   [W] : Mover para cima           |
|   [S] : Mover para baixo          |
|   [A] : Mover para esquerda       |
|   [D] : Mover para direita        |
|                                   |
|   [E] : Tirar foto                |
|   [Q] : Mostrar status atual      |
|   [M] : Mostrar mapa              |
|                                   |
|   [BACKSPACE] : Voltar            |
|===================================|
|     REFERÊNCIA DE COORDENADAS     |
|-----------------------------------|
|     0X                            |
|   0Y █ █ █ . . █ . . . . . .      |
|      . . . █ . . . █ . . . .      |
|      . █ . . █ . █ . █ . . .      |
|      . . █ . . █ . . . █ . .      |
|      █ . . █ . . █ . . . █ .      |
|      . █ . . █ . . █ █ █ █ .      |
|      . . █ . █ . . . . . . .      |   
+-----------------------------------+
""")
        if keyboard.is_pressed('backspace'):
            self.ismenu = True
            self.ym = 1

    def exit(self):
        if keyboard.is_pressed('enter'):
            sys.exit(0)

menu = Menu()
