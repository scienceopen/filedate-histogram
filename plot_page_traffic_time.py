#!/usr/bin/env python
"""
plots traffic from Statcounter .csv download

https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
"""
import pandas
from matplotlib.pyplot import show
from pathlib import Path
import argparse


def load(fn: Path) -> pandas.Series:
    fn = Path(fn).expanduser()
    df = pandas.read_csv(
        fn, skiprows=2, usecols=[0, 1], parse_dates=[[0, 1]], header=None, names=["date", "time"], index_col=0
    ).squeeze()
    df["hits"] = 1  # each hit is one
    hits = df.groupby(pandas.Grouper(freq="1D")).count()

    return hits


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("fn", help=".csv file")
    P = p.parse_args()

    dat = load(P.fn)

    dat.plot()

    show()
