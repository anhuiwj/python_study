import os
'''
编写一个函数，用递归的方法输出斐波那契额数列第n项
'''
def fblq(len,index=2,index0 = 1,index1=1,index2 = 0):    
    print("index %d"%index)
    if(index < len):
       index2 = index0 + index1
       index0 =  index1
       index1 = index2
       print(index2)
       index += 1
       fblq(len,index,index0,index1,index2)          
print(fblq(5))
    
