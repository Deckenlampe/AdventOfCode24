filename = 'Input6.txt'
map_standard = []

with open(filename, 'r') as file:
    for line in file:
        map_standard.append(list(line.strip()))

global direction
global cnt
cnt = 0
def find_start(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '^':
                return i, j
    return -100, -100

def detect_end(x, y, direction, array):
    if direction == 'up' and x == 0:
        return True
    elif direction == 'down' and x == len(array) - 1:
        return True
    elif direction == 'left' and y == 0:
        return True
    elif direction == 'right' and y == len(array[x]) - 1:
        return True
    else:
        return False


def move_up(x, y, array):
    if not detect_end(x, y, "up", array):
        return x - 1, y
    else:
        return -100, -100


def move_down(x, y, array):
    if not detect_end(x, y, "down", array):
        return x + 1, y
    else:
        return -100, -100


def move_left(x, y, array):
    if not detect_end(x, y, "left", array):
        return x, y - 1
    else:
        return -100, -100


def move_right(x, y, array):
    if not detect_end(x, y, "right", array):
        return x, y + 1
    else:
        return -100, -100


def change_direction(direction):
    if direction == 'up':
        direction = 'right'
    elif direction == 'right':
        direction = 'down'
    elif direction == 'down':
        direction = 'left'
    elif direction == 'left':
        direction = 'up'

    return direction


def object_ahead(x, y, direction, array):
    if direction == 'up' and array[x - 1][y] == '#':
        return True
    elif direction == 'down' and array[x + 1][y] == '#':
        return True
    elif direction == 'left' and array[x][y - 1] == '#':
        return True
    elif direction == 'right' and array[x][y + 1] == '#':
        return True
    else:
        return False

def field_marked(x, y, array):
    if array[x][y] != 'X':
        array[x][y] = 'X'
        return False
    return True

def move_one_step(x, y, direction, array):
    if direction == 'up':
        return(move_up(x, y, array))
    elif direction == 'right':
        return(move_right(x, y, array))
    elif direction == 'down':
        return(move_down(x, y, array))
    elif direction == 'left':
        return(move_left(x, y, array))

def main(array):
    direction = 'up'
    cnt = 0
    in_map = True
    x, y = find_start(array)
    if x == -100 and y == -100:
        print("Kein Start gefunden")
        return

    while in_map:
        if not field_marked(x, y, array):
            cnt += 1
        if not detect_end(x, y, direction, array):
            if not object_ahead(x, y, direction, array):
                x, y = move_one_step(x, y, direction, array)
            elif object_ahead(x, y, direction, array):
                direction = change_direction(direction)
        else:
            in_map = False
            print("out of map")
    return cnt


def new_ahead (x, y, direction, array):
    if direction == 'up' and array[x - 1][y] == 'O':
        return True
    elif direction == 'down' and array[x + 1][y] == 'O':
        return True
    elif direction == 'left' and array[x][y - 1] == 'O':
        return True
    elif direction == 'right' and array[x][y + 1] == 'O':
        return True
    else:
        return False

def mark_object(x, y, direction, array):
    if direction == 'up':
        array[x - 1][y] = 'O'
    elif direction == 'down':
        array[x + 1][y] = 'O'
    elif direction == 'left':
        array[x][y - 1] = 'O'
    elif direction == 'right':
        array[x][y + 1] = 'O'

def endless_loop(array):
    endless = 0
    k = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'X':
                array_2 = []

                with open(filename, 'r') as file:
                    for line in file:
                        array_2.append(list(line.strip()))

                x, y = find_start(array_2)
                direction = 'up'
                array_2[i][j] = 'O'
                in_map = True
                right = 0
                left = 0
                up = 0
                down = 0
                k += 1
                while in_map:
                    if not detect_end(x, y, direction, array_2):
                        if not object_ahead(x, y, direction, array_2) and not new_ahead(x, y, direction, array_2):
                            x, y = move_one_step(x, y, direction, array_2)
                        elif object_ahead(x, y, direction, array_2):
                            mark_object(x, y, direction, array_2)
                            direction = change_direction(direction)
                        elif new_ahead(x, y, direction, array_2):
                            if direction == 'up':
                                up += 1
                                direction = change_direction(direction)
                            elif direction == 'right':
                                right += 1
                                direction = change_direction(direction)
                            elif direction == 'down':
                                down += 1
                                direction = change_direction(direction)
                            elif direction == 'left':
                                left += 1
                                direction = change_direction(direction)

                        if up > 100 or right > 100 or left > 100 or down > 100:
                            print("endless detected", k)
                            in_map = False
                            endless += 1
                    else:
                        in_map = False
                        print("out of map")

    return endless

main(map_standard)

print(endless_loop(map_standard))




