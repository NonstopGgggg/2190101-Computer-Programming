# We are given a list and we are to group the elements by their last digit.
# We are to return a list of 10 lists where each list contains the elements that have the same last digit.
def to_buckets(d):
    buckets = [[] for _ in range(10)]

    for i in d:
        buckets[i%10].append(i)

    return buckets

print(to_buckets([12, 25, 33, 47, 51, 62, 74, 88, 91, 100]))
