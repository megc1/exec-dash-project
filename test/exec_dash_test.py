import os
import pytest
import pandas

from app.monthly_sales import to_usd, get_top_sellers
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

def test_get_top_sellers():
    CSV_FILENAME = "sales-201904.csv"
    CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "test_data", CSV_FILENAME)
    df = pandas.read_csv(CSV_FILEPATH)
    results = get_top_sellers(df)
    expected_result = [
        {'name': 'Button-Down Shirt', 'monthly sales': 5008.849999999999},
        {'name': 'Super Soft Hoodie', 'monthly sales': 1800.0},
        {'name': 'Khaki Pants', 'monthly sales': 1691.0},
        {'name': 'Vintage Logo Tee', 'monthly sales': 877.25},
        {'name': 'Brown Boots', 'monthly sales': 250.0},
        {'name': 'Sticker Pack', 'monthly sales': 220.5},
        {'name': 'Baseball Cap', 'monthly sales': 156.31}
    ]
    assert results == expected_result