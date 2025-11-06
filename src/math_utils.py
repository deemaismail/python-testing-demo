def add_numbers(numbers):
    """ترجع مجموع كل الأرقام في القائمة"""
    return sum(numbers)

def average(numbers):
    """تحسب المعدّل باستخدام الدالة add_numbers"""
    total = add_numbers(numbers)
    return total / len(numbers)
