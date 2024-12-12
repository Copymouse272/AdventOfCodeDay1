

#open file
santa = open('2015\day 1\input.txt', 'r')
#read file
santa = santa.read()
#set floor level
floor_count = 0

for character in santa:
    if character == '(':
        floor_count += 1
    elif character == ')':
        floor_count += -1


print("Floor is:", floor_count)

