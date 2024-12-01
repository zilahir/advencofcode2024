def main():
    arr1 = []
    arr2 = []
    # arr1 = [3, 4, 2, 1, 3, 3]
    # arr2 = [4, 3, 5, 3, 9, 3]

    # load input file

    with open("input.txt", "r") as file:
        for line in file:
            # Split each line into columns
            columns = line.split()

            # Skip empty lines
            if len(columns) == 2:
                colA, colB = map(int, columns)  # Convert to integers
                arr1.append(colA)
                arr2.append(colB)

    # distance = []

    similartyscores = []

    if len(arr1) != len(arr2):
        print("Arrays are not of same length")
        return

    # for i in range(len(arr1)):
    #     sm1 = min(arr1)
    #     sm2 = min(arr2)
    #
    #     distance.append(abs(sm1 - sm2))
    #
    #     arr1.remove(sm1)
    #     arr2.remove(sm2)
    #
    # # print the distance array
    # sum_distance = 0
    # for i in range(len(distance)):
    #     sum_distance += distance[i]
    #
    # print("Sum of distances between the two arrays is: ", sum_distance)

    for i in range(len(arr1)):
        this_number = arr1[i]
        # count the number of times this_number appears in arr2
        count = arr2.count(this_number)
        similartyscores.append(this_number * count)

    sum_similarity = 0
    for i in range(len(similartyscores)):
        sum_similarity += similartyscores[i]

    print("Sum of similarity scores between the two arrays is: ", sum_similarity)


if __name__ == "__main__":
    main()
