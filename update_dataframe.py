# -*- coding: utf-8 -*-

"""
更新dataframe中的值
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


def update_column():
    df = get_df()
    print(df)

    # 新增一列
    df["E"] = 1
    print(df)

    # 按label修改
    df.loc["2020-01-01", ["A", "B"]] = 1
    print(df)

    # 按位置修改
    df.iloc[1, :] = 2
    print(df)

    # 使用where条件赋值
    df2 = df.copy()
    df2[df2 <= 0] = -df2
    print(df2)


if __name__ == '__main__':
    update_column()
