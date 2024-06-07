# list definetion
bicycles=["jeante","trick",'cannondale']
print(bicycles)

# read elements of list
bicycles=["jeante","trick",'cannondale']
print(bicycles[0])
print(bicycles[1])

# add elements
bicycles=["jeante","trick",'cannondale']
bicycles.append("meilida")
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