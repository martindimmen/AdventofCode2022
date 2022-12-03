rock=1
paper=2
scissors=3
lost=0
draw=3
won=6
points=0

with open ("day2.txt") as file:
    for i in file:
        columns=i.strip()
        columns=columns.split(" ")
        opponent=columns[0]
        me=columns[1]
        #Stein og Stein
        if opponent=="A" and me=="X":
            points+=(rock+draw)
        #Stein og Papir
        elif opponent=="A" and me=="Y":
            points+=(rock+draw)
        #Stein og Saks
        elif opponent=="A" and me=="Z":
            points+=(rock+won)
        #Papir og Stein
        elif opponent=="B" and me=="X":
            points+=(paper+won) 
        #Papir og papir
        elif opponent=="B" and me=="Y":
            points+=(paper+draw)
        #Papir og saks
        elif opponent=="B" and me=="Z":
            points+=(paper+lost) 
        #Saks og stein
        elif opponent=="C" and me=="X":
            points+=(scissors+lost)
        #Saks og Papir
        elif opponent=="C" and me=="Y":
            points+=(scissors+won)
        #Saks og saks
        elif opponent=="C" and me=="Z":
            points+=(scissors+draw)   
print(points)   

