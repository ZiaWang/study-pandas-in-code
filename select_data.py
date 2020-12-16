# -*- coding: utf-8 -*-

"""
从dataframe中获取数据
"""
from __future__ import print_function

import pandas as pd
import numpy as np


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


def select_column():
    df = get_df()
    print(df)

    col_a = df["A"]
    print(type(col_a))
    print(col_a)

    print(col_a[0])
    print(col_a["2020-01-01"])


def select_rows():
    df = get_df()
    print(df)

    sub_df = df[0: 3]
    print(sub_df)

    sub_df = df["2020-01-01": "2020-01-03"]
    print(sub_df)


def select_by_label():
    df = get_df()
    print(df)

    # 选择一行数据
    row = df.loc["2020-01-01"]
    print(row)

    # 选择指定某行的指定列
    row_col = df.loc["2020-01-01", ["A", "B"]]
    print(row_col)

    # 选择指定列的多行数据数据
    sub_df = df.loc["2020-01-01": "2020-01-03", ["A", "B"]]
    print(sub_df)

    dates = pd.date_range("20200101", periods=6)

    # 使用df.at获取指定位置的值
    val = df.at[dates[0], "A"]
    print(val)

    # 使用df.at获取指定位置的值
    val = df.at[dates[1], "A"]
    print(val)

    val = df.at[pd.Timestamp("20200101"), "A"]
    print(val)


def select_by_condition():
    df = get_df()
    print(df)

    sub_df = df[df.A > 0]
    print(sub_df)

    sub_df = df[df > 0]
    print(sub_df)

    df2 = df.copy()
    df2["E"] = list("aabbcc")
    print(df2)

    sub_df = df2[df2["E"].isin(["a", "b"])]
    print(sub_df)


def select_by_idx():
    pass


if __name__ == '__main__':
    select_by_condition()
