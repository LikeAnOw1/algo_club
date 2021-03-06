# gathering info
input_string = input()

house = [int(n) for n in input_string.split(' ')]
#house = list([5, 7, 8, 6, 8, 9, 8, 4])

cash = list([]) # payday so far
prev = list([]) # best previous house
luckies = list([]) # house numbers start with 1, NOT 0. We're humans after all

# planning
for pp in range(len(house)):
    if (pp == 0):
        cash.append(house[pp])
        prev.append(0)
    elif (pp == 1):
        cash.append(house[pp])
        prev.append(0)
    elif (pp == 2):
        cash.append(house[pp] + cash[pp-2])
        prev.append(pp-2+1)
    elif (pp > 2) :
        cash.append(house[pp] + max(cash[pp-2], cash[pp-3]))
        prev.append(cash.index(max(cash[pp-2], cash[pp-3])) + 1)
        
#print(prev)
#print(cash)

# execution
if (len(house) == 1):
    payday = cash[0]
    luckies.append(1)
    
else:
    payday = max(cash[-1], cash[-2])
    luckies.append(cash.index(max(cash[-1], cash[-2]))+1)
    while (prev[luckies[-1] - 1] > 0):
        luckies.append(prev[luckies[-1] - 1])
    
luckies.sort()
print(' '.join(str(qq) for qq in luckies))

# queue the music
print(payday)