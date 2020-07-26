"""
Testing the is_equal function

execute test on command line with:
> pytest test_is_equal.py
"""

import os
os.chdir("/".join(__file__.split("/")[:-1]))
import sys
sys.path.append("../")

from is_equal import is_equal

import pandas as pd
import numpy as np

def test_DataFrames():
    df1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
    df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
    assert is_equal(df1,df2)

def test_list_and_dicts():
    test1 = [{"a":1,"b":2}, 10, [1,2,[4,5,6]]]
    test2 = [{"a":1,"b":2}, 10, [1,2,[4,5,6]]]
    assert is_equal(test1,test2)

def test_list_and_dicts_not_equal():
    test1 = [{"a":1,"b":2}, 10, [1,4,[4,5,6]]]
    test2 = [{"a":1,"b":2}, 10, [1,2,[4,5,6]]]
    assert not is_equal(test1,test2)

if __name__=="__main__":
    test_DataFrames()
    test_list_and_dicts()
    test_list_and_dicts_not_equal()