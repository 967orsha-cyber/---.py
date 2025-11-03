field = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
symbols = {0: " ", 1: "X", 2: "O"}

def print_field():
    print("\n   0 1 2")    # отображаем с 0 для координатной сетки
    for i, row in enumerate(field):
        print(f"{i}  {' '.join(symbols[cell] for cell in row)}")

def get_move(player):
    while True:
        try:
            row = int(input("Ряд (1-3): ")) - 1  # запрос ввода
            col = int(input("Позиция (1-3): ")) - 1
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if field[row][col] == 0:
                    field[row][col] = player
                    return
                else:
                    print("Занято!")
            else:
                print("Только 1, 2 или 3!")
        except ValueError:
            print("Вводите числа!")

def check_win(player):
    # Проверка строк
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] == player:
            return True
            
    # Проверка столбцов  
    for j in range(3):
        if field[0][j] == field[1][j] == field[2][j] == player:
            return True
            
    # Проверка диагоналей
    if field[0][0] == field[1][1] == field[2][2] == player:
        return True
    if field[0][2] == field[1][1] == field[2][0] == player:
        return True
        
    return False

def is_draw():
    for row in field:
        for cell in row:
            if cell == 0:
                return False
    return True

# Главный цикл игры
current_player = 1

while True:
    print_field()
    print(f"\nХод игрока {symbols[current_player]}")
    
    get_move(current_player)
    
    if check_win(current_player):
        print_field()
        print(f"Игрок {symbols[current_player]} победил!")
        break
    
    if is_draw():
        print_field()
        print("Ничья!")
        break
    
    current_player = 3 - current_player

input("\nНажмите Enter чтобы выйти...")
