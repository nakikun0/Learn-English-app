import csv
import pprint

def saver(dict):

    with open('En_datas.csv','w',encoding='utf-8') as f:
        for word in dict:
            f.write(word + "\n")
    
    with open("Jp_datas.csv",'w',encoding='utf-8') as f:
        for word in dict:
            f.write(dict[word] + "\n")

import testapp.views