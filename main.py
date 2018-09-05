import os as os
from pathlib import Path
import pandas as pd
import numpy as np

correct_path = os.path.isdir("/Users/nicholasrotondo/documents/file_crawler")

def isTrueBool():
    if correct_path == True:
        print("This is true!")
    else:
        print("Not true")

def crawl_dir():
    folders = []
    files_list = []
    df = pd.read_excel("./virus_ext.xlsx")
    file_ext = df.iloc[:,0]


    for root, dirs, files in os.walk("/"):
        for file in files:
            if file.endswith(file_ext):
                path_to_file = os.path.join(root, file)
                print(path_to_file)

    print(files_list)
