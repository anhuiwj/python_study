print('找出七个各个数位上数字相加是9的偶数：')

i,len = 0,0
while True:
    i += 1
    if i%2==1: continue
    cs, ci = 0, i
    while ci>0:
        cs += ci%10
        ci //= 10
    if cs == 9:
        len += 1
        print(i)
        if len==7:break
    
