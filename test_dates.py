#!/usr/bin/env python
import pytest
from pathlib import Path
from datetime import datetime
import filedate as fd

R = Path(__file__)


def test_gitdates():
    date = fd.get_gitcommit_date(R)
    assert isinstance(date, datetime)


if __name__ == "__main__":
    pytest.main([__file__])
