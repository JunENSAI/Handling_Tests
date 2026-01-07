import pytest

from src.date_parser import standardize_date


@pytest.mark.parametrize(
    "raw_input, expected_output",
    [
        ("12/01/2023", "2023-12-01"),
        ("2023.12.01", "2023-12-01"),
        ("01/30/2020", "2020-01-30"), 
    ],
)
def test_valid_date_formats(raw_input, expected_output):
    assert standardize_date(raw_input) == expected_output


@pytest.mark.parametrize(
    "raw_input",
    [
        "invalid",
        "2023/12/01",
        "13/01/2023",
    ],
)
def test_invalid_dates(raw_input):
    with pytest.raises(ValueError):
        standardize_date(raw_input)
