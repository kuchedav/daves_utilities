import pandas as pd
import numpy as np

def is_equal_recursive(elem1,elem2):
    if(type(elem1) != type(elem2)):
        return False
    if(isinstance(elem1,list)):
        if len(elem1) != len(elem2):
            return False
        return [is_equal_recursive(i,j) for i,j in zip(elem1,elem2)]
    elif(isinstance(elem1,dict)):
        if len(elem1) != len(elem2):
            return False
        elem1_in = list(elem1.values())
        elem2_in = list(elem2.values())
        return [is_equal_recursive(i,j) for i,j in zip(elem1_in,elem2_in)]
    elif(isinstance(elem1,int) or isinstance(elem1,float) or isinstance(elem1,str)):
        return elem1 == elem2
    elif "pandas" in str(type(elem1)):
        if elem1.shape != elem2.shape:
            return False
        return elem1.equals(elem2)
    elif "sklearn" in str(type(elem1)):
        return str(elem1) == str(elem2)

def list_flatten(l, a=None):
    if a is None: a = []
    l = [l] if isinstance(l,bool) else l
    for i in l:
        if isinstance(i, list):
            list_flatten(i, a)
        else:
            a.append(i)
    return a

def is_equal(elem1,elem2,flatten = True):
    boolen_list = is_equal_recursive(elem1,elem2)
    
    if flatten: return all(list_flatten(boolen_list))
    else: return boolen_list

if __name__=="__main__":
    df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])

    test1 = [{"a":1,"b":2}, 10, [1,2,[4,5,6]], df2]
    test2 = [{"a":1,"b":2}, 10, [1,2,[4,5,6]], df2]
    
    out = is_equal(test1,test2)
    print(out)