import string

Lcase=dict(zip(string.ascii_lowercase,range(1,27)))
Ucase = dict(zip(string.ascii_uppercase, range(27, 53)))
thedict=Lcase | Ucase
usedletter=list()
sum=0


with open ("day3.txt","r") as file:
    for i in file:
        i=i.strip()
        bag=list(i)
        middlepoint=(len(bag))//2
        f_half=bag[:middlepoint]
        s_half=bag[middlepoint:]
        for k in f_half:
            for j in s_half:
                if k==j:
                    if j in usedletter:
                        break
                    else:
                        sum+=(thedict[k])
                        usedletter.append(j)
        usedletter.clear()
print(sum)
