import os
'''
编写一个函数，生成一个斐波那契数列前n项的list
'''
def fblq(len):
    ls = []
    index0 = 1
    index1 = 1
    index2 = 0
    ls.append(0)
    ls.append(1)
    for o in range(1,len):
       index2 = index0 + index1
       index0 =  index1
       index1 = index2
       ls.append(index2)
    return ls
print(fblq(3))
    
