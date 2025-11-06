from src.math_utils import add_numbers, average

def test_average_integration():
    numbers = [2, 4, 6, 8]

    total = add_numbers(numbers)
    avg = average(numbers)

    # تحقق من أن التكامل بين الدالتين يعمل صح
    assert total == 20
    assert avg == 5
