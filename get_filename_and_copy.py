import os
import shutil


filepat="E:\\MRI_DATA"                             #原文件夹路径
st1="3D-t1"                                                  #要提取的文件夹所包含的字符组成
pathne="F:\\3D-T1"                                         #目标文件夹路径
    
""" 
在目标文件夹中提取含有某字符串命名的文件夹下所有文件 
"""
def FindAndCopy(filepath,str1,pathnew,count=1000):         #count 表示要提取的相关文件夹的数量，默认1000
    file1list=os.walk(filepath)                            #遍历filepath下的所有文件路径，将其写入file1list
    count0=0                                               #文件夹数量计数
    for path,d,filelist in file1list:
        #print("正在读取数据")
        for filename in filelist:                          #filename文件名字
            k=os.path.join(path, filename)                 #path为最底层文件夹路径，filename为文件名
            #print(k)
            #path==k
            ls=path[11:]                                   #截取path路径的从第十一位起后面的字符串 ，存入ls （相当于保留原来的命名文件夹命名规律）                    
            #print(type(path))                             #test
            if(str1 in path):                              #如果要查找的文件夹名存在与查找的文件中
                pathnew1=pathnew+ls                        #构建新的存储路径
                isExists=os.path.exists(pathnew1)          #判断新的路径是否存在
                if not isExists:
                    os.makedirs(pathnew1)
                    shutil.copy(k,pathnew1)
                    count0=count0+1                        #每创建一个文件夹计数器加1，若原来存在该文件夹，计数器不会变化，慎用
                    print("正在复制提取第",count0,"个文件夹的内容")
                    
                else:
                    shutil.copy(k,pathnew1)
                    #print("copying")
            else:
                pass
        if(count0>=count):                                  #如果提取文件夹数量满足要求，退出，默认count=1000
            break
""" 
在目标文件夹中提取含有某字符串命名的文件夹下所有文件 
"""

FindAndCopy(filepat,st1,pathne,3)