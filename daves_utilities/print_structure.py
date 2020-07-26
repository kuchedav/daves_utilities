"""
print_structure prints out the structure of any arbitrary python object.
"""

__version__ = "0.0.3"

import numpy as np
import pandas as pd

def print_str(object_atr, print_elements = False, level = 0):
    """
    print_str is the wrapper command which recoursively calles itself,
        as well as the print function.
    """

    if isinstance(object_atr, (str,int,float,bool,complex,bytes,memoryview)):
        if print_elements: print_level_type(object_atr,level)
        else: return
    elif isinstance(object_atr,(pd.core.frame.DataFrame,pd.core.series.Series)):
        print_level_type(object_atr,level)
        if isinstance(object_atr,pd.core.frame.DataFrame):
            if print_elements: [print_level_type(i,level+1,pandas_dtype=j) for i,j in zip(object_atr.columns,object_atr.dtypes)]
    elif isinstance(object_atr,(list,tuple,range,set,frozenset,bytearray)):
        print_level_type(object_atr,level)
        [print_str(i,print_elements,level+1) for i in object_atr]
    elif isinstance(object_atr,dict):
        print_level_type(object_atr,level)
        elem1_in = list(object_atr.values())
        [print_str(i,print_elements,level+1) for i in elem1_in]
    elif isinstance(object_atr,np.ndarray):
        print_level_type(object_atr,level)
    
def get_shape(input_elem) -> str:
    if isinstance(input_elem,(list,dict,tuple,set,frozenset,range,bytearray)):
        return "("+str(len(input_elem))+")"
    elif isinstance(input_elem,(pd.core.frame.DataFrame,pd.core.series.Series,np.ndarray)):
        return str(input_elem.shape)
    else:
        return ""

def print_level_type(input_elem,level,pandas_dtype = None):
    # get shape
    shape_out = get_shape(input_elem)
    
    # create indentation
    level_indent = ""
    if level > 0:
        level_indent = "  " * level
    level_indent = level_indent + "|___"
    type_string = str(type(input_elem)).split("'")[1]

    # if pandas columns are given
    if pandas_dtype:
        level = ""
        level_indent += "__"
        type_string = f"{input_elem} - {pandas_dtype}"

    # create print statement
    print_color = f"{level_indent}{level} [{type_string}] {shape_out}"
    
    print(print_color)

if __name__=="__main__":
    """
    Testing the print_structure function

    execute test on command line with:
    > pytest test_print_structure.py
    """

    from ..print_structure import print_str

    # pandas data
    df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
    data = np.array(['a','b','c','d'])
    s = pd.Series(data)

    # numpy data
    np_array = np.array([[1, 2], [3, 4]])

    # complex numbers
    complex_n = 2+3j
    # boolean
    boolean_var = True
    # tuple
    tuple_var = (1,3,4)
    # set
    set_var = set((1,2,4))
    # range
    range_var = range(0,3)

    ### bytes
    simple_bytes_string = b"test_test"
    string = "Pyth"
    bytes_arr = bytearray(string, 'utf-8')
    mem_var = memoryview(simple_bytes_string)

    test1 = [{"a":1,"b":2}, 10, [1,2,[4,5,6,[1,3,["string","test",[1,[1,[1]]]]]]], \
        df2, [s], np_array, complex_n, boolean_var, tuple_var, set_var, range_var, \
            simple_bytes_string, bytes_arr, mem_var]

    print_str(object_atr = test1)