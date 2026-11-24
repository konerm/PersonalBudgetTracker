from main import calculate_balance, calculate_expenses

def test_calculate_expenses():
    assert calculate_expenses([1000, 200, 300]) == 1500

def test_empty_expenses():
    assert calculate_expenses([]) == 0

def test_positive_balance():
    assert calculate_balance(3000, 1500) == 1500

def test_zero_balance():
    assert calculate_balance(1000, 1000) == 0

def test_negative_balance():
    assert calculate_balance(1000, 1500) == -500