'''
用埃拉托色尼筛输出0-n的质数的list
'''

def zs(length):
 
    li = list(range(length))

    newli = []

    res = []
    
    index = 2
    for k in range(0,length):
        for i in range(0,len(li)):
            if(li[i] == 0 or li[i] == 1 ): newli.append(li[i]) 
            if(li[i] != index and li[i] % index == 0):newli.append(li[i])
        index += 1
    
    for s in range(0,len(li)-1):
            if(li[s] not in newli):res.append(li[s])
    return res
 
print(zs(100))
