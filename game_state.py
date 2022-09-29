WIN_CONDITION = 3


def retrieve_game_result(game_state_string, playing_field):
    game_result = None
    x_victory = has_won_game(playing_field, "X")
    o_victory = has_won_game(playing_field, "O")

    if x_victory and not o_victory:
        game_result = "X wins"
    elif o_victory and not x_victory:
        game_result = "O wins"
    else:
        if is_draw(x_victory, o_victory, game_state_string):
            game_result = "Draw"
        elif is_impossible(x_victory, o_victory, game_state_string):
            game_result = "Impossible"
        elif is_unfinished_game(x_victory, o_victory, game_state_string):
            game_result = "Game not finished"

    return game_result


def has_won_game(playing_field, character_to_check):
    row_victory = is_row_win(playing_field, character_to_check)
    column_victory = is_column_win(playing_field, character_to_check)
    main_diagonal_victory = is_main_diagonal_win(playing_field, character_to_check)
    secondary_diagonal_victory = is_secondary_diagonal_win(playing_field, character_to_check)

    return row_victory or column_victory or main_diagonal_victory or secondary_diagonal_victory


def is_row_win(playing_field, character_to_check):
    count = 0
    for row in range(len(playing_field)):
        count = 0
        for col in range(len(playing_field[0])):
            if playing_field[row][col] == character_to_check:
                count += 1
            if count == WIN_CONDITION:
                return True

    return False


def is_column_win(playing_field, character_to_check):
    count = 0
    for col in range(len(playing_field[0])):
        count = 0
        for row in range(len(playing_field)):
            if playing_field[row][col] == character_to_check:
                count += 1
            if count == WIN_CONDITION:
                return True

    return False


def is_main_diagonal_win(playing_field, character_to_check):
    count = 0
    for row in range(len(playing_field)):
        for col in range(len(playing_field[0])):
            if row == col:
                if playing_field[row][col] == character_to_check:
                    count += 1
            if count == WIN_CONDITION:
                return True

    return False


def is_secondary_diagonal_win(playing_field, character_to_check):
    count = 0
    for row in range(len(playing_field)):
        for col in range(len(playing_field[0])):
            if row + col == len(playing_field[0]) - 1:
                if playing_field[row][col] == character_to_check:
                    count += 1
            if count == WIN_CONDITION:
                return True

    return False


# Checks if no side has a three in a row and there are no empty cells
def is_draw(x_victory, o_victory, game_state_string):
    has_empty_cells = " " in game_state_string

    if not x_victory and not o_victory and not has_empty_cells:
        return True

    return False


def is_unfinished_game(x_victory, o_victory, game_state_string):
    has_empty_cells = "_" in game_state_string

    if not x_victory and not o_victory and has_empty_cells:
        return True

    return False


def is_impossible(x_victory, o_victory, game_state_string):
    x_count = game_state_string.count('X')
    o_count = game_state_string.count("O")
    difference = x_count - o_count
    max_difference = 1

    if abs(difference) > max_difference or (x_victory and o_victory):
        return True

    return False


def is_occupied_cell(playing_field, row, col):
    # Converts user input to match the 0 based index system
    row -= 1
    col -= 1

    return playing_field[row][col] == "X" or playing_field[row][col] == "O"


def is_full_playing_field(playing_field, empty_char):
    empty_cells = 0

    for row in range(len(playing_field)):
        for col in range(len(playing_field[row])):
            if playing_field[row][col] == empty_char:
                empty_cells += 1
                break;

    return empty_cells == 0


def update_playing_field(playing_field, row, col, value_to_insert):
    # Converts user input to match the 0 based index system
    row -= 1
    col -= 1

    playing_field[row][col] = value_to_insert

