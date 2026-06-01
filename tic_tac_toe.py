class Player:
    def __init__(self):
        self.name = ''
        self.symbol = ''
    
    def choose_name(self, player_label):
        while True:
                name = input(f'{player_label}, please enter your name (letters only): ')
                if name.isalpha():
                    self.name = name
                    break
                print('Invalid name. Please enter letters only.')  
    def choose_symbol(self, player_label):
        while True:
                symbol = input(f'{player_label}, choose your symbol (single letter): ')
                if symbol.isalpha() and len(symbol)==1:
                    self.symbol = symbol.upper()
                    break
                print('Invalid symbol. Please enter one letter only.')

class Menu:
    def display_main_menu(self):
        print('welcome to the game ')
        print('1.Satrt the game')
        print('2.Quit the game')
        choice=input('enter your choice(1 or 2):')
        return choice

    def display_endgame_menu(self):
        print('game over ')
        print('1.Restart the game')
        print('2.Quit the game')
        choice=input('enter your choice(1 or 2):')
        return choice

class Board:
    def __init__(self):
        self.board=[str(i) for i in range(1,10) ]
    def display_board(self):
        for i in range(0, 9, 3):
            print('|'.join(self.board[i:i + 3]))
            if i < 6:
                print('-' * 5)   #1|2|3
                                 #-----
                                 #4|5|6
                                 #-----
                                 #7|8|9
    def update_board(self,choice,symbol):
        if self.is_valid_move(choice):
            self.board[choice-1]=symbol
            return True
        return False
    def is_valid_move(self,choice):
        return  self.board[choice-1].isdigit() # solid Principle ---->Single Responsibility Principle
    def reset(self):
        self.board=[str(i) for i in range(1,10) ]

    def check_winner(self):
        win_lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        ]
        for a, b, c in win_lines:
            if self.board[a] == self.board[b] == self.board[c] and not self.board[a].isdigit():
                return self.board[a]
        return None

    def is_draw(self):
        return self.check_winner() is None and all(not cell.isdigit() for cell in self.board)

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0  # ← بيبدأ بالأول دايماً
    def start_game(self):
        choice=self.menu.display_main_menu()
        if choice=='1':
            self.setup_player()
            self.play_game()
        else:
            self.quit_game()
    def setup_player(self):
        for index, player in enumerate(self.players, start=1):
            player_label = f'Player {index}'
            print(f'\n--- {player_label} setup ---')
            player.choose_name(player_label)
            player.choose_symbol(player_label)
    def play_game(self):
        self.board.reset()
        self.current_player_index = 0

        while True:
            self.board.display_board()
            current_player = self.players[self.current_player_index]
            self._get_player_move(current_player)

            winner_symbol = self.board.check_winner()
            if winner_symbol:
                self.board.display_board()
                winner = next(p for p in self.players if p.symbol == winner_symbol)
                print(f'\n{winner.name} wins! Congratulations!')
                break

            if self.board.is_draw():
                self.board.display_board()
                print("\nIt's a draw!")
                break

            self.current_player_index = 1 - self.current_player_index

        self.handle_endgame()

    def _get_player_move(self, player):
        while True:
            try:
                choice = int(input(f"{player.name} ({player.symbol}), enter position (1-9): "))
            except ValueError:
                print('Please enter a number from 1 to 9.')
                continue
            if choice < 1 or choice > 9:
                print('Position must be between 1 and 9.')
                continue
            if self.board.update_board(choice, player.symbol):
                return
            print('That cell is taken. Choose an empty cell.')

    def handle_endgame(self):
        while True:
            choice = self.menu.display_endgame_menu()
            if choice == '1':
                self.play_game()
                return
            if choice == '2':
                self.quit_game()
                return
            print('Invalid choice. Please enter 1 or 2.')

    def quit_game(self):
        print('Thank you for playing!')
    
        
      
game =Game()
game.start_game()
          



            
           
       
        


        
    
    
         












        