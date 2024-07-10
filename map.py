class Ocean:
    def __init__(self):
        self.grid = [
            [1, 1, 1, 5, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 4, 0, 0],
            [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [2, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 1, 3, 0, 0, 0, 0, 0, 0]
        ]

    def print_map(self, sub_x, sub_y):
        for y, row in enumerate(self.grid): # y percorre linhas e junta elas, pois tem múltiplas linhas, row pega fila inteira de cada uma
            for x, cell in enumerate(row): # x percorre colunas e junta elas, cell pega o valor de cada coluna em uma única linha (a fila inteira que foi pega)
                if x == sub_x and y == sub_y:
                    print(".", end=" ") # Submarino está aqui
                elif cell == 1:
                    print("█", end=" ") # Formata com um quadrado o texto
                elif cell in [2, 3, 4, 5]:
                    print("@", end=" ")
                else:
                    print(".", end=" ")
            print()

    def is_wall(self, x, y):
        if y < 0 or y >= len(self.grid) or x < 0 or x >= len(self.grid[0]): #Caso vá fora dos limites
            return True  #Fora dos limites é considerado parede
        return self.grid[y][x] == 1 #É parede também no 1, retorna falso caso não seja == 1 (não é parede)

    def get_object_type(self, x, y):
        cell_value = self.grid[y][x]
        if cell_value in [2, 3, 4, 5]:
            return cell_value
        return None

    def is_valid_move(self, x, y):
        return not self.is_wall(x, y) #Se der falso, fica true, se der true, fica false