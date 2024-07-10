from submarine import Submarine
from map import Ocean
from menu import Menu
import time
import pygame
import sys


class Game:
    def __init__(self):
        self.submarine = Submarine()
        self.ocean = Ocean()
        self.menu = Menu()
        self.is_running = False
        self.music = False

    def run(self):
        while True:
            if self.music == False:
                pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
                pygame.mixer.music.load("sounds/main/music.mp3")
                pygame.mixer.music.play(loops = -1)
                
                self.music = True
            if not self.is_running:
                if self.menu.ismenu == True:
                    self.menu.text()
                if self.menu.ym == 1 and self.menu.start(): #self.menu.start() caso retorne true
                    
                    self.is_running = True
                    self.game_loop() #executa o loop
                if self.menu.ym == 2:
                    self.menu.controls() #Executa o método de mostrar a tela de controles
                if self.menu.ym == 3:
                    self.menu.exit() #Executa o método de sair
            else:
                break  # Sai do loop quando o jogo termina

    def game_loop(self): #Loop do movimento do submarino
        while self.is_running:
            self.submarine.move(self.ocean) #Monitora movimento no oceano
            if self.submarine.oxygen <= 0:
                print("Fim de jogo! Oxigênio esgotado.")
                time.sleep(10)
                sys.exit(0)

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
