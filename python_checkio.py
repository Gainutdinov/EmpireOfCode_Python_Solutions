# Hello World program in Python

#def rotate_list(elements, rotates):

#    return elements


import sys
print(sys.version)
rotates =2
elements=[1, 2, 3, 4, 5, 6]
#print(elements.pop(0))
num=0
while num < rotates:
    elements.append(elements[num])
    print(elements[num])
    num += 1

print(elements)
print('\n')

del elements[0:num]

elements.pop(1,2)
print(elements)
