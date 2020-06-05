import pandas as pd
import cv2
import os
import csv
from PIL import Image
List0=['test','train']
for a in range(len(List0)):
    rootdir=os.getcwd()
    rootdird=rootdir + os.sep + List0[a]
    for subdir,dirs,files in os.walk(rootdird):    
        for file in files:
            filepath=subdir+os.sep+file
            if filepath.endswith('.jpeg'):
                im=Image.open(filepath)
                (name,extension)=os.path.splitext(filepath)
                im.save(name+'.jpg')
                os.remove(filepath)
df=pd.read_csv('train2.csv')
for i in range(len(df)):
    df['filename'][i][-1]='g'
    df['filename'][i][-2]='p'
    df['filename'][i][-3]='j'


                

                
