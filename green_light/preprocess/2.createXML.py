
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os

# traiing data related paths
PATH_TRAIN_IN_16KWAVS = '../data/wav/' # frog's 16khz wav forder
PATH_TRAIN_IN_XMLFILES = '../data/xml/' # the path where the XML meta-data files are located

#注意: 要提供物種的 classId mapping 檔(用 species_mapping.xlxs 整理後貼到以 utf-8 編碼的 notepad 後存檔(欄位以 tab \t 分隔)
SPECIES_MAPPING_CSV = '../data/species_mapping.csv'


# In[2]:


df = pd.read_csv(SPECIES_MAPPING_CSV, sep='\t', encoding='utf-8')
df


# In[3]:


for path, subdirs, files in os.walk(PATH_TRAIN_IN_16KWAVS):
    i=1
    for name in files:
        if (name.endswith('.wav')):
            print('#{} - Generating XML for {}'.format(i, os.path.join(path, name)))
            tempFileName = name.split('.')[0]
            cName = name.split('_')[0]
            cId = df[df['chineseName'] == cName]['classId'].item()
            sName = df[df['chineseName'] == cName]['scientificName'].item()
            print('  (cName, cId, sName)=({},{},{})'.format(cName, cId, sName))
            
            tempXmlFile = open(os.path.join(PATH_TRAIN_IN_XMLFILES, tempFileName + '.xml'), 'w', encoding="utf-8")

            tempXmlFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            tempXmlFile.write('<Audio>\n')
            tempXmlFile.write('  <MediaId>{}</MediaId>\n'.format(i))
            tempXmlFile.write('  <FileName>{}.wav</FileName>\n'.format(tempFileName))
            tempXmlFile.write('  <ClassId>{}</ClassId>\n'.format(cId))
            tempXmlFile.write('  <Date>2018-04-12</Date>\n')
            tempXmlFile.write('  <Time>15:00</Time>\n')
            tempXmlFile.write('  <Locality>Taiwan</Locality>\n')
            tempXmlFile.write('  <Latitude>0</Latitude>\n')
            tempXmlFile.write('  <Longitude>0</Longitude>\n')
            tempXmlFile.write('  <Elevation>0</Elevation>\n')
            tempXmlFile.write('  <Author>AIA2018</Author>\n')
            tempXmlFile.write('  <AuthorID>AIA2018</AuthorID>\n')
            tempXmlFile.write('  <Content>song</Content>\n')
            tempXmlFile.write('  <Comments />\n')
            tempXmlFile.write('  <Quality>2</Quality>\n')
            tempXmlFile.write('  <Year>AIA2018</Year>\n')
            tempXmlFile.write('  <BackgroundSpecies>XXXXX</BackgroundSpecies>\n')
            tempXmlFile.write('  <Order>XXXXX</Order>\n')
            tempXmlFile.write('  <Family>XXXXX</Family>\n')
            tempXmlFile.write('  <Genus>Rana</Genus>\n')
            tempXmlFile.write('  <Species>{}</Species>\n'.format(sName))
            tempXmlFile.write('  <Sub-species />\n')
            tempXmlFile.write('  <VernacularNames>XXXXX</VernacularNames>\n')
            tempXmlFile.write('</Audio>\n')

            i += 1
            tempXmlFile.close()

