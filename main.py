""" 
Batle Ships

** plan **

    - create a board
    - create a ship
    - create a player
    - create a computer

"""
import random


class Ship:
    def __init__(self, name, size, id):
        self.name = name
        self.size = size
        self.id = id
        self.hits = 0
        self.sunk = False
        self.x = 0
        self.y = 0
        self.direction = None

    def hit(self):
        self.hits += 1
        if self.hits == self.size:
            self.sunk = True

    def is_sunk(self):
        return self.sunk

class Board:
    def __init__(self):
        self.board = []
        self.dummy_board = []
        self.create_board()
        self.create_dummy_board()

    def create_dummy_board(self):
        for i in range(10):
            self.dummy_board.append([])
            for j in range(10):
                self.dummy_board[i].append(0)

    def create_board(self):
        for i in range(10):
            self.board.append([])
            for j in range(10):
                self.board[i].append(0)

    def add_ship(self, ship):
        if ship.direction == 'h' or ship.direction == 'H':
            for i in range(ship.size):
                self.board[ship.x - 1][ship.y - 1 + i] = ship.id
        else:
            for i in range(ship.size):
                self.board[ship.x - 1 + i][ship.y - 1] = ship.id

    def check_ship_fits(self, ship):
        try:
            if ship.direction == 'h' or ship.direction == 'H':
                if ship.x + ship.size > 10:
                    return False
                for i in range(ship.size):
                    if self.board[ship.x - 1][ship.y - 1 + i] != 0:
                        return False
            else:
                if ship.y + ship.size > 10:
                    return False
                for i in range(ship.size):
                    if self.board[ship.x - 1 + i][ship.y - 1] != 0:
                        return False
            return True
        except IndexError:
            return False
                
    def print_board(self):
        print('     1  2  3  4  5  6  7  8  9  10')
        print('  -------------------------------------')
        count = 0
        for i in self.board:
            count += 1
            if count == 10:
                print(f"{count}: ", end='')
                for j in i:
                    print(f" {j}", end=' ')
            else:
                print(f" {count}: ", end='')
                for j in i:
                    print(f" {j}", end=' ')
            print()
            
            

    def print_dummy_board(self):
        print('    1  2  3  4  5  6  7  8  9  10')
        print('  -------------------------------------')
        count = 0
        for i in self.dummy_board:
            count += 1
            if count == 10:
                print(f"{count}: ", end='')
                for j in i:
                    print(f" {j}", end=' ')
            else:
                print(f" {count}: ", end='')
                for j in i:
                    print(f" {j}", end=' ')
            print()
class Player:
    def __init__(self, name):
        self.name = name
        self.ships = []
        self.create_ships()

    def create_ships(self):
        self.ships.append(Ship("Carrier", 6, 1))
        self.ships.append(Ship("Battleship", 5, 2))
        self.ships.append(Ship("Cruiser", 4, 3))
        self.ships.append(Ship("Submarine", 3, 4))
        self.ships.append(Ship("Destroyer", 2, 5))

    def print_ships(self):
        for ship in self.ships:
            print(ship.name)

class Computer:
    def __init__(self, name):
        self.name = name
        self.ships = []
        self.create_ships()

    def create_ships(self):
        self.ships.append(Ship("Carrier", 6, 1))
        self.ships.append(Ship("Battleship", 5, 2))
        self.ships.append(Ship("Cruiser", 4, 3))
        self.ships.append(Ship("Submarine", 3, 4))
        self.ships.append(Ship("Destroyer", 2, 5))

    def place_ships(self, board):
        for ship in self.ships:
            while True:
                ship.x = random.randint(1, 10)
                ship.y = random.randint(1, 10)
                ship.direction = random.choice(['h', 'V'])
                if board.check_ship_fits(ship):
                    board.add_ship(ship)
                    break

    def print_ships(self):
        for ship in self.ships:
            print(ship.name)

def user_auto_add(board, player):
    for ship in player.ships:
        ship.x = random.randint(1, 10)
        ship.y = random.randint(1, 10)
        ship.direction = random.choice(['h', 'V'])
        if board.check_ship_fits(ship):
            board.add_ship(ship)

def user_add_ship_to_board(board, player):
        for ship in player.ships:
            ok = False
            while ok == False:
                print(board.print_board())
                # print ship details
                print(f"ship name >> {ship.name}\nShip size >> {ship.size}")
                # ask for ship direction
                ship.direction = input("Enter direction (h/v): ")
                # ask for ship position
                ship.y = int(input("Enter y: "))
                ship.x = int(input("Enter x: "))
                # check if ship fits on board
                if board.check_ship_fits(ship):
                    board.add_ship(ship)
                    ok = True
                else:
                    print("Ship does not fit in board or overlaps with other ships")

def user_take_shot(ComBoard, userBoard):
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    if ComBoard.board[x - 1][y - 1] == 0:
        print("------------------")
        print("You missed")
        print("------------------")
        userBoard.dummy_board[x - 1][y - 1] = 'M'
        print()
    else:
        print("------------------")
        print("You hit")
        print("------------------")
        userBoard.dummy_board[x - 1][y - 1] = 'H'
        print()
    
    userBoard.print_dummy_board()
    
def computer_take_shot(userBoard, ComBoard):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    if userBoard.board[x - 1][y - 1] == 0:
        print("\n\n------------------")
        print("Computer missed")
        print("------------------")
        ComBoard.dummy_board[x - 1][y - 1] = 'M'
        userBoard.board[x - 1][y - 1] = 'M'
        print()
    else:
        print("------------------")
        print("Computer hit")
        print("------------------")
        ComBoard.dummy_board[x - 1][y - 1] = 'H'
        userBoard.board[x - 1][y - 1] = 'H',
        print()
    
    userBoard.print_board()

def main():
    UserBoard = Board()
    ComputerBoard = Board()
    User = Player("Player")
    computer = Computer("Computer")

    computer.place_ships(ComputerBoard)
    user_auto_add(UserBoard, User)
    game_ended = False
    while game_ended == False:
        user_take_shot(ComputerBoard, UserBoard)
        computer_take_shot(UserBoard, ComputerBoard)
        if UserBoard.board.count('H') == 16:
            print("You won!")
            game_ended = True
        if ComputerBoard.board.count('H') == 16:
            print("Computer won!")
            game_ended = True
        

    



if __name__ == "__main__":
    main()


