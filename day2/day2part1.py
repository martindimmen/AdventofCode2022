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
        if opponent=="A" and me=="X":
            points+=(rock+draw)
        
        elif opponent=="A" and me=="Y":
            points+=(rock+draw)
        
        elif opponent=="A" and me=="Z":
            points+=(rock+won)
        
        elif opponent=="B" and me=="X":
            points+=(paper+won) 
        
        elif opponent=="B" and me=="Y":
            points+=(paper+draw)
        
        elif opponent=="B" and me=="Z":
            points+=(paper+lost) 
        
        elif opponent=="C" and me=="X":
            points+=(scissors+lost)
        
        elif opponent=="C" and me=="Y":
            points+=(scissors+won)
        
        elif opponent=="C" and me=="Z":
            points+=(scissors+draw)   
print(points)   

