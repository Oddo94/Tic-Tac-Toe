import re
import game_state
import data_validation

MAX_ROWS = 3
MAX_COLUMNS = 3
MAX_CHARACTERS = 9


def generate_empty_playing_field(rows, cols):
    playing_field = [[0 for i in range(rows)] for j in range(cols)]

    for i in range(len(playing_field)):
        for j in range(len(playing_field[i])):
            playing_field[i][j] = " "

    return playing_field


def display(playing_field):
    print("---------")
    for i in range(len(playing_field)):
        print("|", end=" ")
        for j in range(len(playing_field[i])):
            print(playing_field[i][j], sep=" ", end=" ")

        print("|", end= " ")
        print()

    print("---------")


def to_string(playing_field):
    characters_list = []
    for row in range(len(playing_field)):
        for col in range(len(playing_field[row])):
            characters_list.append(playing_field[row][col])

    return "".join(characters_list)


def run_game():
    playing_field = generate_empty_playing_field(MAX_ROWS, MAX_COLUMNS)
    display(playing_field)

    current_player = "X"
    while True:
        coordinates = input()
        # Checks if user input is valid with regard to the characters introduced and the coordinates values
        if data_validation.check_user_coordinates(coordinates) == -1:
            continue

        coordinates_list = [int(element) for element in coordinates.split(" ")]
        row = coordinates_list[0]
        col = coordinates_list[1]

        # Checks if the position indicated by the coordinates is occupied
        if game_state.is_occupied_cell(playing_field, row, col):
            print("This cell is occupied! Choose another one!")
            continue
        else:
            # Updates the playing field
            game_state.update_playing_field(playing_field, row, col, current_player)
            display(playing_field)

        game_state_string = to_string(playing_field)
        game_result = game_state.retrieve_game_result(game_state_string, playing_field)

        # Checks game result
        if game_result != None:
            print(game_result)
            break;

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def manage_game():
    run_game()


manage_game()


