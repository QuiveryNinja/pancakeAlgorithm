pancakes = [2,3,1,7,4,0,5]
plate = []

def SortPancakes():
    pancakes.sort()
    i = 0
    while i in pancakes:
        plate.append(pancakes[-1])
        pancakes.pop(-1)
    for i in plate:
        if i == 0:
            plate.pop(i)
    
    return plate

print(SortPancakes())
