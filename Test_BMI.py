import Lab2.BMI as bmi

def test_bmi_normal_weight():
    weight = 68
    height = 1.75
    calculated_bmi , cls  = bmi.calculate_bmi(weight,height)
    assert cls == 0

def test_bmi_underweight():
    weight = 50
    height = 1.85
    calculated_bmi , cls  = bmi.calculate_bmi(weight,height)
    assert cls == -1

def test_bmi_over_weight():
    weight = 90
    height = 1.5
    calculated_bmi , cls  = bmi.calculate_bmi(weight,height)
    assert cls == 1

