# input: 2:3, 4:4
# return: [[2.0, 3.0], [4.0, 4.0]]

def read_points(string):
    # Split the points into pairs of coordinate
    points = []
    pairs = string.split(",")

    for pair in pairs:
        # Assign X and Y value from the pair to the list of coordinate
        # First element is X, and the second element is Y
        x,y = pair.split(":")
        x = float(x)
        y = float(y)

        points.append([x,y])

    return points

print(read_points("2:3, 4:4"))
