# -*- coding: utf-8 -*-

"""
创建pd.Series
"""
import numpy as np
import pandas as pd


def create_series():
    s_of_object = pd.Series([1, 3, 5, 7, "", None])

    s_of_int64 = pd.Series([1, 2, 3, 4])

    s_of_float64 = pd.Series([1, 2, 3, 4, np.nan])

    assert isinstance(np.nan, float)


def create_series_with_index():
    s = pd.Series([1, 2, 3], index=["a", "b", "c"])
    print(s)
    assert s.a == 1
    assert s.b == 2
    assert s["a"] == 1
    assert s["b"] == 2

    assert s[0] == s['a'] == s.a


if __name__ == '__main__':
    create_series_with_index()
