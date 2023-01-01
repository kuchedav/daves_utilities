import numpy as np
import pandas as pd

from daves_utilities import is_equal


def test_is_equal():
    df2 = pd.DataFrame(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["a", "b", "c"]
    )

    test1 = [{"a": 1, "b": 2}, 10, [1, 2, [4, 5, 6]], df2]
    test2 = [{"a": 1, "b": 2}, 10, [1, 2, [4, 5, 6]], df2]

    assert is_equal(test1, test2)
