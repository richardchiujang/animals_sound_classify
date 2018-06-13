
# coding: utf-8

# In[1]:


import os
from shutil import copyfile
get_ipython().system('pwd')


# In[2]:


# 定義原來依中文學名存放各物種聲音檔的來源目錄
dirPath = '../data/orig/'
# 定義要複製到攤平的一階目錄名 (會將原檔名前加上原子目錄的中文學名 ex: 八哥/wave0001.wav --> 八哥_wave0001.wav)
copy2Path = '../data/wav/'
# 將跑過的子目錄中文學名寫入檔案, 供後續編輯 specise_mapping.csv 用
speciesListCSV = '../data/species_list.csv'


# In[3]:


if os.path.exists(copy2Path) is False:
    os.mkdir(copy2Path)

tempFile = open(speciesListCSV, 'w', encoding="utf-8")
tempFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')

sNum=0
fNum=0
for path, subdirs, files in os.walk(dirPath):
    for sub in subdirs:
        tempFile.write('{}\n'.format(sub))
        sNum+=1
        for p, s, f in os.walk(dirPath + sub):
            for name in f:
                if (name.endswith('.wav')):
                    srcPathName = p + '/' + name
                    toPathName = copy2Path + sub + '_' + name
                    print('p={}, s={}, name={}'.format(p,s,name))
                    print('  └copy and rename file:{}\n                    -->:{}\n'.format(srcPathName, toPathName))
                    copyfile(srcPathName, toPathName)
                    fNum+=1
tempFile.close()
print('--- 處理結束: 共處理了 {} 個物種子目錄, {} 個 wav 檔'.format(sNum, fNum))

