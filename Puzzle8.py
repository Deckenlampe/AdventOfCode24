filename = 'Input8.txt'
antennas = []

with open(filename, 'r') as file:
    for line in file:
        antennas.append(list(line.strip()))
def mark_field(x, y, map):
    if x < 0 or x >= len(map):
        return False
    if y < 0 or y >= len(map[x]):
        return False
    if map[x][y] == ".":
        map[x][y] = "#"
        return True
    return False


def find_parallel(frequence, map, x, y):
    cnt = 0
    antennas = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == frequence and (i != x or j != y):
                distance = [abs(x - i), abs(y - j)]
                distance_2 = [x-i, y-j]
                if mark_field(x + distance_2[0], y + distance_2[1], map):
                    cnt += 1
                if mark_field(i - distance_2[0], j - distance_2[1], map):
                    cnt += 1
                """
                if x > i and y > j:
                    if mark_field(x+distance[0], y+distance[1], map):
                        cnt += 1
                    if mark_field(i-distance[0], j-distance[1], map):
                        cnt += 1
                elif x < i and y < j:
                    if mark_field(x-distance[0], y-distance[1], map):
                        cnt += 1
                    if mark_field(i+distance[0], j+distance[1], map):
                        cnt += 1
                elif x > i and y < j:
                    if mark_field(x+distance[0], y-distance[1], map):
                        cnt += 1
                    if mark_field(i-distance[0], j+distance[1], map):
                        cnt += 1
                elif x < i and y > j:
                    if mark_field(x-distance[0], y+distance[1], map):
                        cnt += 1
                    if mark_field(i + distance[0], j - distance[1], map):
                        cnt += 1
                elif x == i:
                    if y < j:
                        if mark_field(x, y-distance[1], map):
                            cnt += 1
                        if mark_field(i, j+distance[1], map):
                            cnt += 1
                    else:
                        if mark_field(x, y + distance[1], map):
                            cnt += 1
                        if mark_field(i, j - distance[1], map):
                            cnt += 1
                elif y == j:
                    if x < i:
                        if mark_field(x - distance[0], y, map):
                            cnt += 1
                        if mark_field(i + distance[0], j, map):
                            cnt += 1
                    else:
                        if mark_field(x + distance[0], y, map):
                            cnt += 1
                        if mark_field(i - distance[0], j, map):
                            cnt += 1
             
                else:
                    print("else??")
                """
    return cnt

def map_through(map):
    antennas = []
    cnt = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != "." and map[i][j] != "#":
                frequence = map[i][j]
                cnt += find_parallel(frequence, map, i, j)
    return cnt

print(map_through(antennas))
print(antennas)
