# Given a list of names, print all possible pairs of names
# Let's say the input is "A, B, C, D"
# The output should be:
# A vs B | A vs C | A vs D
# B vs C | B vs D 
# C vs D
# We notice that after pairing A with everyone, we don't need to pair A again.
# Similarly for B, after pairing with C and D, we don't need to pair B again.
# This means we can use two loops, the outer loop for the first name and the inner loop for the second name starting after the first name.

s = input().split(', ')
n = len(s)

#outer loop for the first name
for i in range(n):

    # inner loop for the second name starting after the first name
    for j in range(i+1,n):
        print(s[i],"vs",s[j])
