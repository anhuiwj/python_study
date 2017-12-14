import os
'''
作业4：编写一个函数，输出某个目录下面的文件层级
作业5：在4基础上，能完整的输出子文件夹以及文件
'''
def outfiles(path):
    ls = os.scandir(path);
    for i in ls:
        if(i.is_dir()):
            print(i.path)
            outfiles(i.path)
        elif(i.is_file() or len(os.listdir(i.path)) == 0): print(i.path)

outfiles("/Users/wangjie/workspace/python学习/python_study")
    
