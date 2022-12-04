import string

templist=[]
mainlist=[]
usedletter=[]
sum=0
counter=0
var0=None
var1=None
var2=None

Lcase=dict(zip(string.ascii_lowercase,range(1,27)))
Ucase = dict(zip(string.ascii_uppercase, range(27, 53)))
thedict=Lcase | Ucase

with open ("day3.txt","r") as file:
    for i in file:
        stripped=i.strip()
        counter+=1
        templist.append(stripped)
        if counter==3:
            for j in templist:
                mainlist.append(j)
            counter=0
            templist.clear()
            for k in range(3):
                if  k==0:
                    var0=mainlist[0]
                elif k==1:
                    var1=mainlist[1]
                else:
                    var2=mainlist[2]
            mainlist.clear()
            for a in var0:
                for b in var1:
                    for c in var2:
                        if a==b==c:
                            if a in usedletter:
                                break
                            else:
                                usedletter.append(a)
                                sum+=(thedict[a])                    
            usedletter.clear()
            var0=None
            var1=None
            var2=None
print(sum)