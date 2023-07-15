import numpy as np


def is_equal_recursive(elem1, elem2):  # noqa
    if type(elem1) != type(elem2):
        return False
    if isinstance(elem1, list):
        if len(elem1) != len(elem2):
            return False
        return [is_equal_recursive(i, j) for i, j in zip(elem1, elem2)]
    elif isinstance(elem1, dict):
        if len(elem1) != len(elem2):
            return False
        elem1_in = list(elem1.values())
        elem2_in = list(elem2.values())
        return [is_equal_recursive(i, j) for i, j in zip(elem1_in, elem2_in)]
    elif isinstance(elem1, np.ndarray):
        return (elem1 == elem2).all()
    elif "pandas" in str(type(elem1)):
        if elem1.shape != elem2.shape:
            return False
        return elem1.equals(elem2)
    elif "sklearn" in str(type(elem1)):
        return str(elem1) == str(elem2)
    else:
        try:
            return float(elem1) == float(elem2)
        except Exception as e:
            print("No fitting type for the elements was found!")
            raise e


def list_flatten(l_in, a=None):
    if a is None:
        a = []
    l_in = [l_in] if isinstance(l_in, bool) else l_in
    for i in l_in:
        if isinstance(i, list):
            list_flatten(i, a)
        else:
            a.append(i)
    return a


def is_equal(elem1, elem2, flatten=True):
    boolen_list = is_equal_recursive(elem1, elem2)

    if flatten:
        return all(list_flatten(boolen_list))
    else:
        return boolen_list
