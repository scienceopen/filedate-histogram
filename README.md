# filedate-histogram

[![Actions Status](https://github.com/scivision/filedate-histogram/workflows/ci/badge.svg)](https://github.com/scivision/filedate-histogram/actions)

Plot histogram of dates of files in directory

Just run in a directory to see a histogram of file modified times.
If time method is not specified, use Git commit time if Git is present,
else fallback to file modified time.

## Hugo

Hugo uses header metadata to determine webpage date.

```sh
python filedate.py ~/hugosite/content/posts hugo
```

## Jekyll

Jekyll gets webpage dates from the filename of the Markdown files.

```sh
python filedate.py ~/jekyllsite/_posts/ jekyll
```
