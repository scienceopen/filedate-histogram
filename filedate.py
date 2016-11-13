#!/usr/bin/env python
"""
Plots histogram of dates of files in directory
"""
from pathlib import Path
from datetime import datetime
from pandas import Series

def filedate(path,ext):
    root = Path(p.path).expanduser()
    assert root.is_dir()

    flist = root.glob('*{}'.format(p.ext))
    #flist = sorted(flist)
    #print('found {} files in {}'.format(len(flist),root))

    dates = []
    for f in flist:
        dates.append(datetime.strptime(f.name[:10],'%Y-%m-%d'))

    return Series(dates,name='date')


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('path',help='path to filename to analyze')
    p.add_argument('-e','--ext',help='file extension to analyze',default='.md')
    p = p.parse_args()

    dates = filedates(p.path, p.ext)

    # http://stackoverflow.com/questions/27365467/python-pandas-plot-histogram-of-dates
    dates.groupby([D.dt.year, D.dt.month]).count().plot(kind="bar")

