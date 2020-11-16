from pathlib import Path
from datetime import datetime
import file_date as fd

R = Path(__file__)


def test_header_dates():
    file = R.parent / "tests/hugo.md"
    date = fd.get_markdown_date(file)
    assert date == datetime(2012, 1, 23)


def test_gitdates():
    date = fd.get_gitcommit_date(R)
    assert isinstance(date, datetime)
