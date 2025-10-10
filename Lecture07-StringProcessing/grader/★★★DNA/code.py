# we are given a dna strand and our task is to perform a specific function on it
# the function will be given in the second line of input

# check for invalid input
def is_valid(strand):
    for i in strand:
        if i not in 'ATCG':
            return True
        
    return False

# R = reverse the pair (A with T, C with G and vice versa) and reverse the strand
def reverse_pair(strand):
    newStrand = ''

    for i in range(len(strand)):

        if strand[i] == 'A':
            newStrand += 'T'
        elif strand[i] == 'T':
            newStrand += 'A'
        elif strand[i] == 'C':
            newStrand += 'G'
        elif strand[i] == 'G':
            newStrand += 'C'

    return newStrand[::-1]

# F = find the number of times a specific nucleotide appears in the strand
def find_nucleotide(strand):
    nucleotide = [0,0,0,0] # A, T, G, C

    for i in range(len(strand)):
        if strand[i] == 'A':
            nucleotide[0] += 1
        elif strand[i] == 'T':
            nucleotide[1] += 1
        elif strand[i] == 'G':
            nucleotide[2] += 1
        elif strand[i] == 'C':
            nucleotide[3] += 1
            
    return nucleotide

# D = display the amount of time pairs of nucleotides appear in the strand
def display_pairs(strand, target):
    pairs = 0

    for i in range(len(strand)-1):
        if strand[i:i+2] == target:
            pairs += 1

    return pairs

# input
strand = input().strip().upper()
function = input().strip().upper()

# check for invalid input
if is_valid(strand):
    print("Invalid DNA")

else:
    if function == 'R':
        print(reverse_pair(strand))

    elif function == 'F':
        nucleotide = find_nucleotide(strand)
        print(f"A={nucleotide[0]}, T={nucleotide[1]}, G={nucleotide[2]}, C={nucleotide[3]}")

    elif function == 'D':
        target = input().strip().upper()
        print(display_pairs(strand, target))
