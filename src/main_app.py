def add_numbers(a, b):
    """تجمع رقمين وتتحقق من إنهم أرقام"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("القيم لازم تكون أرقام فقط")
    return a + b

def run_app(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return f"sum = {total}, average = {avg}"
