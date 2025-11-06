def add_numbers(a, b):
    """تجمع رقمين وتتحقق من إنهم أرقام"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("القيم لازم تكون أرقام فقط")
    return a + b
