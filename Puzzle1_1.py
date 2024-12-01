import pandas as pd

# Read the file into a DataFrame
file_path = '/Users/felixwissel/PycharmProjects/CodeOfAdvent/Input1_1.txt'  # Replace with the path to your file
data = pd.read_csv(file_path, delim_whitespace=True, header=None)

# Convert each column into separate arrays
arr1 = data[0].to_list()
arr2 = data[1].to_list()

def calculate_distance(arr1, arr2):
    arr1.sort()
    arr2.sort()

    distance = 0

    for i in range(len(arr1)):
        distance += abs(arr1[i] - arr2[i])
        if i < 5:
            print (arr1[i], " - " ,arr2[i], " = ", abs(arr1[i] - arr2[i]))

    print(distance)
    return distance

def calculate_similarity(arr1, arr2):
    arr1.sort()
    arr2.sort()
    similarity = 0
    count = 0

    for n in arr1:
        for i in range(len(arr2)):
            if n == arr2[i]:
                count += 1
            elif n < arr2[i]:
                similarity += n * count
                count = 0
                break

    print (similarity)
    return similarity

calculate_similarity(arr1, arr2)

