import csv
import pprint

def reader():
    Ens = []
    Jps = []
    mydict = {}

    with open('En_datas.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for word in reader:
            Ens += word

    with open("Jp_datas.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        for word in reader:
            Jps += word

    mydict = dict(zip(Ens,Jps))
    print(mydict)

    return mydict

import testapp.views