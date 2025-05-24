import price_info as price

def test_total_cost_shopping():
    expected_result = 46.75
    result = price.total_cost_shopping()
    assert result == expected_result

def test_cost_of_fruit():
    expected_result = 13
    result = price.cost_of_fruits('watermelon', 2)
    assert result == expected_result