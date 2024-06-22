# list definetion
bicycles=["jeante","trick",'cannondale']
print(bicycles)

# read elements of list
bicycles=["jeante","trick",'cannondale']
print(bicycles[0])
print(bicycles[1])

# add elements,append
bicycles=["jeante","trick",'cannondale']
bicycles.append("meilida")
print(bicycles)

# insert
bicycles=["jeante","trick",'cannondale']
bicycles.insert(1,'manba')
bicycles.insert(0,'meilida')
print(bicycles)

# delete elements, (1)use del 
bicycles=["jeante","trick",'cannondale']
del bicycles[0]
print(bicycles)

# delete elements, (2)use pop, default del the last element,also use index to del any positive element
bicycles=["jeante","trick",'cannondale']
bi_give=bicycles.pop()
print(bicycles)
print(bi_give)

# delete elements, (2)use pop, use index to del any positive element
bicycles=["jeante","trick",'cannondale']
bi_give=bicycles.pop(1)
print(bi_give)
print(bicycles)

# delete elements, (3)use remove, according value to del 
bicycles=["jeante","trick",'cannondale','others','trick']
bicy_give=bicycles.remove('trick')
print(bicycles)

# update
bicycles=["jeante","trick",'cannondale','others','trick']
bicycles[1]='candy'
print(bicycles)

# manage list sort
bicycles=["jeante","trick",'cannondale','others','trick']
bicycles.sort(reverse=True)
print(bicycles)

# manage list sorted
bicycles=["jeante","trick",'cannondale','others','trick']
print(f'temp is {sorted(bicycles,reverse=True)}')
print(bicycles)

# manage list reverse
bicycles=["jeante","trick",'cannondale','others','trick']
print(f'original series is {bicycles}')
bicycles.reverse()
print(f'now is {bicycles}')
bicycles.reverse()
print(f'final is {bicycles}')

# manage list reverse
bicycles=["jeante","trick",'cannondale','others','trick']
print(len(bicycles))