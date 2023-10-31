import price_info


def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    test = 46.75

    assert (result == test)


def test_cost_of_fruit():
    fruit = "orange"
    quantity = 10

    result = price_info.cost_of_fruits(fruit, quantity)
    test = 14

    assert (result == test)
