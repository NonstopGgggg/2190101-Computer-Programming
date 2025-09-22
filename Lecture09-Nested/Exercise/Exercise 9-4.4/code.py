# Accept a list in the form of [[u1,u2], [u3,u4], ...] and return a dictionary {key: value}
def to_dict(like_list):
    d = {}
    for pair in like_list:
        if pair[0] not in d:
            d[pair[0]] = [pair[1]]

        else:
            d[pair[0]] += [pair[1]]
    
    return d

print(to_dict([[1,2], [2,3], [1,4]]))
