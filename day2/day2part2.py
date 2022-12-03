rock=1
paper=2
scissors=3
lost=0
draw=3
won=6
points=0

with open ("day2.txt") as file:
    for i in file:
        columns=i.strip().split(" ")
        elf=columns[0]
        me=columns[1]
        if elf=="A":
            if me=="X":
                points+=(lost+scissors)
            elif me=="Y":
                points+=(draw+rock)
            else:
                points+=(won+paper)
        
        elif elf=="B":
            if me=="X":
                points+=(lost+rock)
            elif me=="Y":
                points+=(draw+paper)
            else:
                points+=(won+scissors)
        
        elif elf=="C":
            if me=="X":
                points+=(lost+paper)
            elif me=="Y":
                points+=(draw+scissors)
            else:
                points+=(won+rock)
print(points)     
