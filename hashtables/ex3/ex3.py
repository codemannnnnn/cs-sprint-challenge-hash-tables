
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = {}
    result = []

    for i in arrays:
        for z in i:
            if z not in hash:
                hash[z] = 1
            else:
                hash[z] += 1

    for i in hash:
        if hash[i] == len(arrays):
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []



    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])


    print(intersection(arrays))
