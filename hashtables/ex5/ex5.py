# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = {}
    result = []

    for i in files:
        hash[i] = 0

    for x in hash:
        for q in queries:
            if q in x:
                result.append(x)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
