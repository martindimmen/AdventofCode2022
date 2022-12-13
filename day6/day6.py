

letters=[]
fours=[]
with open("day6.txt") as file:
    for i in file:
        for j in i:
            letters.append(j)



for x in range(2,(len(letters))):
    fours.append(x)


def sliding_window(elements, window_size):
    counter=0
    counter4=0
    if len(elements) <= window_size:
        return elements
    for i in range(len(elements) - window_size + 1):
        window=(elements[i:i+window_size])
        
        for j in window:
            counter+=1
            if counter%4==0:
                counter4+=1
        if window[0]==window[1] or window[0]==window[2] or window[0]==window[3]:
            print(window)
        elif window[1]==window[0] or window[1]==window[2] or window[1]==window[3]:
            print(window)
        elif window[2]==window[0] or window[2]==window[1] or window[2]==window[3]:
            print(window)
        elif window[3]==window[0] or window[3]==window[1] or window[3]==window[2]:
            print(window)
        else:
            for i in (fours):
                if counter4==i:
                    counter=i+3
                    break
            print("Something unique:",window)
            print(counter)
            break

sliding_window(letters, 4)
