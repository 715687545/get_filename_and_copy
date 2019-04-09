import os
import shutil
filepath="e:\\MRI_DATA"
str1="rest-mri"
str2="svs_se_30_MPF_frontal"
str3="svs_se_30_MPF_occipital"
str4="svs_se_30_MPF_csf"
str5="Occipital_GABA"
str6="mPFC_GABA"
str7="bas_MoCoSeries"
str8="intermediate t-Map"
str9="Design"
str10="EvaSeries_GLM"
pathnew="e:\\MRI_D"
    #path=filepath
    #   path1="/home/xiaohong/dcm-data"
file1list=os.walk(filepath)
for path,d,filelist in file1list:
    print("正在读取数据")
    for filename in filelist:
        k=os.path.join(path, filename)
        print(k)
        path==k
        ls=path[11:]
        print(type(path))
        if(str1 in path or str2 in path or str3 in path or str4 in path or str5 in path or str6 in path or str7 in path or str8 in path or str9 in path or str10 in path):
            pathnew1=pathnew+ls
            isExists=os.path.exists(pathnew1)
            if not isExists:
                os.makedirs(pathnew1)
                shutil.copy(k,pathnew1)
                print("copying")
            else:
                shutil.copy(k,pathnew1)
                print("copying")
        else:
            pass
