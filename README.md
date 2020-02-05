# filedate-histogram

![ci](https://github.com/scivision/filedate-histogram/workflows/ci/badge.svg)

Plot histogram of dates of files in directory

Just run in a directory to see a histogram of file modified times.

```sh
python filedate.py ~/hugosite/content/posts
```

The algorithm determines date of files in a directory, assuming all are the same type, by examining:

1. header metadata
2. filename
3. Git modified time
4. file modification time.
