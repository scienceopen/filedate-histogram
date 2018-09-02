#!/usr/bin/env python
"""
Plots histogram of dates of files in directory

FIXME: git commit time for file with "git log -1 --format=%cd filename"
"""
from pathlib import Path
from datetime import datetime
from pandas import Series
from matplotlib.pyplot import show


def filedates(path: Path, ext: str, jekyll: bool):
    root = Path(p.path).expanduser()
    assert root.is_dir()

    flist = root.glob('*{}'.format(p.ext))

    if jekyll:
        dates = [datetime.strptime(f.name[:10],'%Y-%m-%d') for f in flist]
    else:
        dates = [datetime.utcfromtimestamp(f.stat().st_mtime) for f in flist]

    return Series(dates, name='date')


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('path', help='path to filename to analyze')
    p.add_argument('-e', '--ext', help='file extension to analyze', default='.md')
    p.add_argument('-j', '--jekyll', help='jekyll mode (date from filename)', action='store_true')
    p = p.parse_args()

    dates = filedates(p.path, p.ext, p.jekyll)

    # http://stackoverflow.com/questions/27365467/python-pandas-plot-histogram-of-dates
    dates.groupby([dates.dt.year, dates.dt.month]).count().plot(kind="bar")

    show()
