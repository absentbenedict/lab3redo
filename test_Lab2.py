import Lab2.Lab2 as lab2

def test_calc_average():
    input_list = [5.0 , 4.0]
    result = lab2.calc_average(input_list)
    assert result == 4.5

def test_calc_median_temperature():
    inp_list = [10.0 , 11.0 , 12.0 , 13.0 , 14.0 , 15.0]
    result = lab2.calc_median_temperature(inp_list)
    assert result == 12.5

def test_find_min_max():
    input_list = [10.0 , 20.0 , 35.0 , 12.0 , 9.0]
    result = lab2.find_min_max(input_list)
    assert result == [9.0 , 35.0]