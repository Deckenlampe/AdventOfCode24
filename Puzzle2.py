
# Read the matrix from a file
with open("Input2.txt", "r") as file:
    lines = file.readlines()

# Convert each line into a list of integers
arr = [list(map(int, line.split())) for line in lines]
arr_test = [[18, 21, 22, 24, 26, 29, 28],[48, 51, 54, 56, 60]]
def simple_safe_unsafe(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i][0] < arr[i][1]: #steigend
            for j in range(len(arr[i]) - 1):
                if arr[i][j] >= arr[i][j+1] or arr[i][j + 1] - arr[i][j] > 3:
                    break
                elif arr[i][j] < arr[i][j+1] and j == len(arr[i]) - 2:
                    cnt += 1
                    break
        elif arr[i][0] > arr[i][1]: #fallend
            for j in range(len(arr[i]) - 1):
                if arr[i][j] <= arr[i][j + 1] or arr[i][j] - arr[i][j + 1] > 3:
                    break
                elif arr[i][j] > arr[i][j + 1] and j == len(arr[i]) - 2:
                    cnt += 1
                    break
        else:
            continue
    print(cnt)

def advanced_safe_unsafe(arr):
    cnt = 0
    for i in range(len(arr)):
        if check_safe_1D(arr[i]):
            cnt += 1
        else:
            for j in range(len(arr[i])):
                arr_copy = arr[i].copy()
                del arr_copy[j]
                if check_safe_1D(arr_copy):
                    cnt += 1
                    break
                else:
                    continue
    return cnt

def check_safe_1D(arr):
    if arr[0] < arr[1]: #steigend
        for j in range(len(arr) - 1):
            if arr[j] >= arr[j+1] or arr[j + 1] - arr[j] > 3:
                return False
            elif arr[j] < arr[j+1] and j == len(arr) - 2:
                return True

    elif arr[0] > arr[1]: #fallend
        for j in range(len(arr) - 1):
            if arr[j] <= arr[j + 1] or arr[j] - arr[j + 1] > 3:
                return False
            elif arr[j] > arr[j + 1] and j == len(arr) - 2:
                return True
    else:
        return False



print(advanced_safe_unsafe(arr))