
from bmi import calculate_bmi, get_bmi_category


def test_calculate_bmi():
    bmi = calculate_bmi(70, 1.75)
    assert round(bmi, 2) == 22.86


def test_bmi_zero_height():
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)


def test_get_bmi_category():
    assert get_bmi_category(17) == "Underweight"
    assert get_bmi_category(22) == "Normal"
    assert get_bmi_category(27) == "Overweight"
    assert get_bmi_category(32) == "Obese"
