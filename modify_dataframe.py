# -*- coding: utf-8 -*-

"""
dataframe数据操作
    排序
"""
from __future__ import print_function

import numpy as np
import pandas as pd


def get_df():
    """
                       A         B         C         D
        2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
        2013-01-02  1.212112 -0.173215  0.119209 -1.044236
        2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
        2013-01-04  0.721555 -0.706771 -1.039575  0.271860
        2013-01-05 -0.424972  0.567020  0.276232 -1.087401
        2013-01-06 -0.673690  0.113648 -1.478427  0.524988
    """
    dates = pd.date_range('20200101', periods=6)
    return pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))


def sort_df_index():
    df = get_df()
    print(df)
    print(df.sort_index(axis=0, ascending=False))       # axis = 0，对Y轴操作
    print(df.sort_index(axis=1, ascending=False))       # axis = 1，对X轴操作


def sort_df_values():
    pass


def fill_df():
    df = get_df()

    df2 = df.reindex(index=df.index[:4], columns=list(df.columns) + ["E", ])
    print(df2)

    df_filled = df2.fillna(value=5)
    print(df_filled)

    df2.loc["2020-01-01", "E"] = 1
    df_droped = df2.dropna(how="any")
    print(df_droped)

    print(df2)


if __name__ == '__main__':

    fill_df()






