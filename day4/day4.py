#day4

file="day4.txt"
def opendata(file):
    with open(file) as f:
        data = f.read().splitlines()
    return data

def part1(data):
    counter=0
    for i in data:
        pairs=i.replace("-",",").split(",")
        zero=int(pairs[0])
        one=int(pairs[1])
        two=int(pairs[2])
        three=int(pairs[3])
        if zero<=two and one>=three:
            counter+=1
        elif zero>=two and one<=three:
            counter+=1
    print(counter)

def part2(data):
    counter=0
    for i in data:
        pairs=i.replace("-",",").split(",")
        zero=int(pairs[0])
        one=int(pairs[1])
        two=int(pairs[2])
        three=int(pairs[3])
        if zero==two or zero==three:
            counter+=1
        elif zero<=two and one>=two:
            counter+=1
        elif one==two or one==three:
            counter+=1
        elif zero<three and zero >=two:
            counter+=1 
    print(counter)

if __name__ == "__main__":
    data=opendata(file)
    part1(data)
    part2(data)
#Answers 602 and 891

