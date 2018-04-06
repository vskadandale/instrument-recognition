# all the imports
import os
import urllib
import zipfile
import json
import itertools
import numpy as np
#import matplotlib.pyplot as plt

import essentia
import essentia.standard as es
import pandas as pd #python library for data manipulation and analysis
#import seaborn as sns; # for visualizing data

from sklearn import svm #libraries for machine learning
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.feature_selection import SelectFromModel
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectKBest

#external .py files
import download_file_from_google_drive #for downloading big files from google drive
import confirm_prompt #for confirming user action 
import json_flattener #for flatenning jsons

# [NOTE] Please set the path to dataset here(this is the path to directory where the instrument folders {bas, cel ... vio} will be moved in)
path_to_dataset='../../datasets/good-sounds/instruments'

instruments = os.listdir(path_to_dataset)
instruments.sort()


for instrument in instruments:  
    print("[Instrument] : " + instrument)
    files=sorted(os.listdir(os.path.join(path_to_dataset,instrument)))
    print("Number of files : "+str(len(files)))
    for file in files:
        if(file.endswith('.wav')):
            filename=os.path.join(path_to_dataset,instrument,file) 
            print("Analysing file : "+filename)
            # Compute all features, aggregate only 'mean' and 'stdev' statistics for all low-level, rhythm and tonal frame features
            features, features_frames = es.MusicExtractor(lowlevelSilentFrames='drop',
                                                              lowlevelFrameSize=2048,
                                                              lowlevelHopSize=1024,
                                                              lowlevelStats=['mean', 'stdev'])(filename)
            features_frames=[]
            es.YamlOutput(filename = filename.replace('.wav','.json'), format='json')(features)
            features=[]
            filename=[]
    print("Feature Extraction Completed Successfully")


