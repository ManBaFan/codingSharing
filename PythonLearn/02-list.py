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
# slice
print(bicycles[1:3])
print(bicycles[:3])
print(bicycles[3:5])
print(bicycles[-3:])

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

# iterate list 
bicycles=["jeante","trick",'cannondale','others','trick']
for bicycle in bicycles:
    print(f'bicycle name is {bicycle}\n')
print('there are all bicycles')

bicycles=["jeante","trick",'cannondale','others','trick']
print(f'it is {bicycles}')

for i in range(1,5):
    print(f'i name is {i}')

# create int list
numbers = list(range(1,6))
print(numbers)

# create even number
even_num = list(range(2,11,2))
print(even_num)

# create square list
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(f'this is squares {squares}')

# as simply as, list comprehension
squares = [square**2 for square in range(1,11)]
print(squares)
 
# list statistics
digital = [2,4,5,1,6,3,7,0]
sum(digital)
max(digital)
min(digital)

# num 20
for num in range(1,21):
    print(num)

# num 1,000,000
nums = list(range(1,1000001))
max(nums)
min(nums)
sum(nums)
for num in nums:
    print(f'this is {num}\n')

# create 1-20 odd number
o_nums = list(range(1,21,2))
print(o_nums)
for num in o_nums:
    print(num)

# create num list ,3-30 num%3=0
three_nums = list(range(3,31,3))
print(three_nums)
for i in three_nums:
    print(i)

nums = []
for num in range(3,31):
    if num%3 == 0:
        nums.append(num)
print(nums)

# create list of  third power,and for print
# list conprehension
third_pow = [value**3 for value in range(1,11)]
for i in third_pow:
    print(i)

# foods copy list
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods
# friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
print('my favorite food is:')
for i in my_foods:
    print(i)
print('\nfriends favorite food is:')
for i in friend_foods:
    print(i)