""" 
Batle Ships

** plan **

    - create a board
    - create a ship
    - create a player
    - create a computer

"""


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
        self.create_board()

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
                
    def print_board(self):
        print('    1  2  3  4  5  6  7  8  9  10')
        for i in range(10):
            # conver i to a letter
            print(f"{i + 1}: {self.board[i]}")

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

    def add_ship_to_board(self, board):
        for ship in self.ships:
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


                

    def print_ships(self):
        for ship in self.ships:
            print(ship.name)


board = Board()
player = Player("Player")

player.add_ship_to_board(board)



