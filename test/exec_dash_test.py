import os
import pytest

from app.monthly_sales import to_usd
#Reference: Prof. Rossetti's example solution

def test_to_usd():
    #test format
    assert to_usd(2.11) == "$2.11"
    #test decimal places
    assert to_usd(2.1) == "$2.10"
    #test rounding
    assert to_usd(2.148) == "$2.15"
    #test thousands separators
    assert to_usd(222333.456) == "$222,333.46"