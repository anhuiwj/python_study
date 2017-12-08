'''
1. 质数是只能被1和它本身整出的数，编程找出100以内全部的质数。
2. 斐波那契数列是两个1构成，从第三项开始，每一项是由前面两项的和构成，如下：1，1，2，3，5...
    请通过编程得到数列的前100项，并输出99项与100项的比值。
'''

def zs(fw):
    fw += 1
    for i in range(2,fw):
        #对于从2到fw之间的数，每个数都拿来除以从2到它自身一半（i/2）的所有数，看是否能被整除；
        for k in range(2,int(fw/2)):
            if i%k == 0:break
        #如果2-100之间的某个数，除了1 和它本身之外，没有其他可以整除的数，则是质数
        if k > int(i/2):   
            print(i)

print('100以内全部的质数:') 
zs(100)

def fblq(len):
    index0 = 1
    index1 = 1
    index2 = 0
    index99 = 0;
    index100 = 0;
    for o in range(1,len):
       index2 = index0 + index1
       index0 =  index1
       index1 = index2
       print(index2)
       if(o == 99):
           index99 = index2
       if(o == 100):
           index100 = index2
    print("99项与100项")
    print(index99/index100)

print('100以内全部的质数:') 
fblq(101)
        


