#!/usr/bin/env python
"""
Plots histogram of dates of files in directory.

Works for Hugo, Jekyll and Git.
"""
from pathlib import Path
from datetime import datetime
import yaml
import re
import shutil
import typing
import subprocess

try:
    import pandas
    from matplotlib.pyplot import show
except ImportError:
    pandas = show = None

GIT = shutil.which("git")


def filedates(path: Path, ext: str, ftype: str) -> typing.List[datetime]:
    root = Path(p.path).expanduser()
    assert root.is_dir()

    files = root.glob("*{}".format(p.ext))

    if ftype == "jekyll":
        dates = [datetime.strptime(f.name[:10], "%Y-%m-%d") for f in files]
    elif ftype == "hugo":
        dates = [get_markdown_date(f) for f in files]
    elif GIT is not None:
        dates = [get_gitcommit_date(f) for f in files]
    else:
        dates = [datetime.utcfromtimestamp(f.stat().st_mtime) for f in files]

    return dates


def get_markdown_date(path: Path) -> datetime:
    content = path.read_text(errors="ignore")
    pat = re.compile(r"^-{3}\s*\n([\S\s]+?)\n-{3}\s*\n([\S\s]+)")

    mat = pat.search(content)
    if mat:
        meta = yaml.load(mat.groups()[0], Loader=yaml.BaseLoader)
        if "date" in meta:
            return datetime.strptime(meta["date"], "%Y-%m-%d")

    return datetime.utcfromtimestamp(path.stat().st_mtime)


def get_gitcommit_date(path: Path) -> datetime:

    if not path.is_file():
        return None

    cmd = [GIT, "-C", str(path.parent), "log", "-1", "--format=%cd", "--date=iso", path.name]
    datestr = subprocess.check_output(cmd, universal_newlines=True)
    try:
        date = datetime.strptime(datestr[:10], "%Y-%m-%d")
    except ValueError:
        date = None

    return date


if __name__ == "__main__":
    from argparse import ArgumentParser

    p = ArgumentParser()
    p.add_argument("path", help="path to filename to analyze")
    p.add_argument("ftype", help="filetype e.g. [hugo, jekyll]", nargs="?")
    p.add_argument("-e", "--ext", help="file extension to analyze", default=".md")
    p = p.parse_args()

    dates = filedates(p.path, p.ext, p.ftype)

    if pandas is not None:
        # http://stackoverflow.com/questions/27365467/python-pandas-plot-histogram-of-dates
        ds = pandas.Series(dates)
        bins = ds.groupby([ds.dt.year, ds.dt.month]).count()
        if show is not None:
            bins.plot(kind="bar")
            show()
