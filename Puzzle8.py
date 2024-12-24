filename = 'Input8.txt'
antennas = []

with open(filename, 'r') as file:
    for line in file:
        antennas.append(list(line.strip()))

marked = []
marked_2 = []

def mark_field2(x, y, map):
    if x < 0 or x >= len(map):
        return False
    if y < 0 or y >= len(map[x]):
        return False
    if [x,y] in marked:
        return False
    return True


def save_marked(frequence, map, x, y):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == frequence and (i != x or j != y):
                distance_2 = [x - i, y - j]
                if mark_field2(x + distance_2[0], y + distance_2[1], map):
                    marked.append([x + distance_2[0], y + distance_2[1]])
                if mark_field2(i - distance_2[0], j - distance_2[1], map):
                    marked.append([i - distance_2[0], j - distance_2[1]])

def map_through(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != "." and map[i][j] != "#":
                frequence = map[i][j]
                save_marked(frequence, map, i, j)


def out_of_bounds(x, y, map):
    if x < 0 or x >= len(map):
        return True
    elif y < 0 or y >= len(map[x]):
        return True
    return False

def field_in_marked(x, y):
    if [x,y] in marked_2:
        return True
    return False

def mark_every_field(frequence, map, x, y):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == frequence and (i != x or j != y):

                distance = [x - i, y - j]
                inbound = True

                temp_position_1 = [x, y]
                temp_position_2 = [i, j]

                while inbound:
                    # temp_position_1 = [temp_position_1[0] + distance[0], temp_position_1[1] + distance[1]]
                    # temp_position_2 = [temp_position_2[0] - distance[0], temp_position_2[1] - distance[1]]
                    if (out_of_bounds(temp_position_1[0], temp_position_1[1], map)
                            and out_of_bounds(temp_position_2[0],temp_position_2[1], map)):
                        inbound = False
                    if not out_of_bounds(temp_position_1[0], temp_position_1[1], map) \
                             and not field_in_marked(temp_position_1[0], temp_position_1[1]):
                        marked_2.append([temp_position_1[0], temp_position_1[1]])
                        temp_position_1 = [temp_position_1[0] + distance[0], temp_position_1[1] + distance[1]]
                    if not out_of_bounds(temp_position_2[0], temp_position_2[1], map) \
                              and not field_in_marked(temp_position_2[0], temp_position_2[1]):
                        marked_2.append([temp_position_2[0], temp_position_2[1]])
                        temp_position_2 = [temp_position_2[0] - distance[0],temp_position_2[1] - distance[1]]
                    temp_position_1 = [temp_position_1[0] + distance[0], temp_position_1[1] + distance[1]]
                    temp_position_2 = [temp_position_2[0] - distance[0], temp_position_2[1] - distance[1]]

def map_through2(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != ".":
                frequence = map[i][j]
                mark_every_field(frequence, map, i, j)

map_through2(antennas)
print(len(marked_2))



