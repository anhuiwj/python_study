'''
用埃拉托色尼筛输出0-n的质数的list
'''

def zs(length):
    li = {}
    li = list(range(length))

    sm = 0
    for i in range(0,len(li)-1):
        if(li[i] ==  0 or li[i] ==  1):
            li.remove(i)
            continue
        sm = li[i]
        if(li[i] % sm == 0):li.remove(i)
        
    return li
 
print(zs(100))
