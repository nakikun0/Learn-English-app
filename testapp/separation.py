def sep_EN(mydict):
    EN = {}
    i = 0
    for word in mydict:
        EN[i] = mydict[word]
        i += 1
    
    return EN

def sep_JP(mydict):
    JP = {}
    i = 0
    for word in mydict:
        JP[i] = word
        i += 1
    
    return JP