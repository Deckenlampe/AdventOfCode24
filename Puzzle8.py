filename = 'Input8.txt'
antennas = []

with open(filename, 'r') as file:
    for line in file:
        antennas.append(list(line.strip()))

marked = []

def mark_field2(x, y, map):
    if x < 0 or x >= len(map):
        return False
    if y < 0 or y >= len(map[x]):
        return False
    if [x,y] in marked:
        return False
    return True


def find_parallel(frequence, map, x, y):
    cnt = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == frequence and (i != x or j != y):
                distance_2 = [x-i, y-j]
                if mark_field(x + distance_2[0], y + distance_2[1], map):
                    cnt += 1
                if mark_field(i - distance_2[0], j - distance_2[1], map):
                    cnt += 1
    return cnt

def save_marked(frequence, map, x, y):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == frequence and (i != x or j != y):
                distance_2 = [x - i, y - j]
                if mark_field2(x + distance_2[0], y + distance_2[1], map):
                    marked.append([x + distance_2[0], y + distance_2[1]])
                if mark_field2(i - distance_2[0], j - distance_2[1], map):
                    marked.append([i - distance_2[0], j - distance_2[1]])

def map_through2(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != "." and map[i][j] != "#":
                frequence = map[i][j]
                save_marked(frequence, map, i, j)

map_through2(antennas)
print(len(marked))