"""
Testing the fun_save function

execute test on command line with:
> pytest test_fun_save.py
"""

import os
os.chdir("/".join(__file__.split("/")[:-1]))
import sys
sys.path.append("../")

from fun_save import fun_save

import pandas as pd
import numpy as np

def test_testing_structure():
    pass

def test_simple_function_default_path():
    # fun_save(fun_input = concatenate_input, attr_input = input_values)
    pass


if __name__=="__main__":
    input_values = {"embeddings":["tf-idf","word2vec","doc2vec","bert"]}

    # function to apply
    def concatenate_input(embeddings):
        return f"{embeddings}"

    # output = fun_save(fun_input = concatenate_input, attr_input = input_values, path = "./daves_utilities/data/", identifier = "")

    test_simple_function_default_path()