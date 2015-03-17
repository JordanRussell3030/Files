import pickle

def load_games(games):
    try:
        with open ("save_game.dat", mode = "rb") as save_game:
            saved = pickle.load(save_game)
            for game in saved:
                games.append(game)
    except FileNotFoundError:
        print("The file cannot be found. ")


def save_games(games):
    with open("save_game.dat", mode = "ab") as save_game:
            pickle.dump(games, save_game)
    pass

#the parameter is games because eventually you will be displaying
#multiple games using this function
class database():
    def __init__(self):
        self.name = None
        self.platform = None
        self.genre = None
        self.cost = None
        self.no_of_players = None
        self.online_functionality = None

def display_games(games):
    print("-" * 131)
    print("|     Name:           Platform:           Genre:           Cost:           Number of players:           Online functionality?     |")
    for game in games:
        print("-" * 131)
        print("|{0:^15} {1:^19} {2:^16} {3:^15} {4:^28} {5:^31}|".format(game.name, game.platform, game.genre, game.cost, game.no_of_players, game.online_functionality))
        print("-" * 131)
    pass

def get_game_from_user(games):
    name = None
    while name != "-1":
        name = input("Please input the name of the game: ")
        if name != "-1":
            game = database()
            game.name = name
            game.platform = input("Please input the platform the game is on: ")
            game.genre = input("Please input the genre of the game: ")
            game.cost = input("Please input the cost of the game: ")
            game.no_of_players = input("Please input the number of players: ")
            game.online_functionality = input("Please state whether the game has online functionality or not: ")
            games.append(game)
    return games
    pass

def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()

def main():
        games = []
        load_games(games)
        exit_program = False
        while not exit_program:
            try:
                display_menu()
                selected_option = int(input("Please select a menu option: "))
                if selected_option == 1:
                    games = get_game_from_user(games)
                    pass
                elif selected_option == 2:
                    display_games(games)
                    pass
                elif selected_option == 3:
                    save_games(games)
                    quit()
                    pass
                else:
                    print("Please enter a valid option (1-3)")
                    print()
            except ValueError:
                print("That is invalid")

if __name__ == "__main__":
    main()
