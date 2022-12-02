calories=0
sumCalories=list()
top3=0

with open ("day1.txt","r") as input:
    for i in input:
        try:
            caloriesint=int(i)
            calories+=caloriesint
        except ValueError:
            sumCalories.append(calories)
            calories=0

sumCalories.sort()

for i in sumCalories[-3:]:
    top3+=i

print(f"Elf with most calories {sumCalories[-1:]}")
print(f"Top 3 elves with most calories {top3}")
