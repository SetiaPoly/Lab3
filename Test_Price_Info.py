import price_info as bob

def test_total_cost_shopping():
    value = bob.total_cost_shopping()
    sample = 46.75

    assert(value == sample)

def test_cost_of_fruits():
    value = bob.cost_of_fruits('pineapple', 69)
    sample = 186.3

    assert(value == sample)


#import price_info as bob

#def test_total_cost_shopping():
#    value = bob.total_cost_shopping()
#    sample = 46.75

#    assert(value == sample)

#def test_cost_of_fruits():
#    quantity = 69
#    expected_result = 69*1.20  #can use that to find the value rather than calculating it
#    value = bob.cost_of_fruits('pineapple', quantity)

#    assert(value == expected_result)
