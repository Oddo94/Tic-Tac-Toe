MAX_COORDINATES = 2

def check_user_coordinates(user_input):
    result = 0
    coordinates = user_input.split(" ")
    row = -1
    col = -1

    if len(coordinates) > MAX_COORDINATES:
        print("You can enter only two coordinates!")
        return -1

    try:
        row = int(coordinates[0])
        col = int(coordinates[1])

    except ValueError:
        print("You should enter numbers!")
        return -1

    if (row < 0 or row > 3) or (col < 0 or col > 3):
        print("Coordinates should be from 1 to 3!")
        return -1
