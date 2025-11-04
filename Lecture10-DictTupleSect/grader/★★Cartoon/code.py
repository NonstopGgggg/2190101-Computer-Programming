# input
animals = {}

while True:
    text = input().strip().split(",")
    
    if text[0] == "q":
        break

    name,animal = text[0], text[1]
    animal = animal.strip()
    
    animals[animal] = animals.get(animal,[]) + [name]

# output
for live in animals:
    print(f"{live}",end=": ")
    
    for i in range(len(animals[live])):
        print(animals[live][i],end="")
        
        if i < len(animals[live])-1:
            print(", ",end="")
            
    print("")
