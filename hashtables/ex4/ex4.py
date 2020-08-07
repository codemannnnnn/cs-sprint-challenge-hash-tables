def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    hash = {}
    result = []

    for i in a:
        abs_val = abs(i)
        if abs_val in hash:
            hash[abs_val] += 1
            result.append(abs_val)
        else:
            hash[abs_val] = 1

    return result

if __name__ == "__main__":
    print(has_negatives([ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]))
