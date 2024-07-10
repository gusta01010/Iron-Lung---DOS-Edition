import keyboard
import time
import winsound
import os
from map import Ocean
from pictures import *

frequency = 150 
duration = 200 

class Submarine:
    def __init__(self, start_x=3, start_y=6):
        self.x = start_x
        self.y = start_y
        self.oxygen = 100.0
        self.progression = 2
        self.Foto_Sapo = SomPlay().picture3
    def showmessage(self, object_type):
        if object_type == self.progression:
            print("TUTORIAL: Você encontrou algo estranho, tire uma foto com [E]")
            self.progression += 1

    def takepicture(self, object_type):
        if keyboard.is_pressed('e'):
            winsound.Beep(frequency+35, duration+900)
            print("Foto tirada!")
            if (object_type == 2): #Se o valor dentro for 2,
                picture1() #Chama a classe picture
            elif (object_type == 3):
                picture2()
            elif (object_type == 4):
                self.Foto_Sapo()
            elif (object_type == 5):
                picture4()
        self.progression = 1
                
    def move(self, ocean): #Pega o oceano para se locomover
        new_x, new_y = self.x, self.y #Os valores novos serão relacionados com a posição atual do submarino

        if keyboard.is_pressed('w'):
            new_y -= 1 #Nova posição
            self.oxygen -= 3.5 #Reduz o nível de oxigênio
            winsound.Beep(frequency, duration) #Toca um som ao se locomover
        if keyboard.is_pressed('s'):
            new_y += 1
            self.oxygen -= 1.5
            winsound.Beep(frequency-20, duration)
        if keyboard.is_pressed('a'):
            self.oxygen -= 2.0
            new_x -= 1
            winsound.Beep(frequency-5, duration)
        if keyboard.is_pressed('d'):
            self.oxygen -= 2.0
            new_x += 1
            winsound.Beep(frequency-5, duration)

        if keyboard.is_pressed('q'):
            time.sleep(0.05)
            winsound.Beep(frequency+75, duration+525)
            print("Localizando...")
            time.sleep(1)
            os.system('cls||clear')
            print (f"X: {self.x}, Y: -{self.y}") #Mostra a posição atual
            print (f"Oxigênio: {self.oxygen:.0f}") #Mostra quantidade de oxigênio sobrando

        if keyboard.is_pressed('m'):
            time.sleep(0.05)
            winsound.Beep(frequency+75, duration+525)
            print("Abrindo mapa...")
            time.sleep(1)
            os.system('cls||clear')
            ocean.print_map(self.x, self.y)

        if ocean.is_valid_move(new_x, new_y): #Recebe os valores dos novos movimentos
            self.x, self.y = new_x, new_y #Atribui os valores com suas respectivas posições atualizadas
            object_type = ocean.get_object_type(self.x, self.y) #
            if object_type: #Se o valor do objeto == true em um dos pontos de interesse
                self.showmessage(object_type) #libera a função do respectivo objeto
                self.takepicture(object_type)
        else:
            print("SENSOR: Estrutura detectada à frente, evitando colisão.") #Se retornar false

        
        time.sleep(0.1) #tempo de espera para evitar spam de teclas
