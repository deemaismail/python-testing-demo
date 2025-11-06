from src.main_app import run_app

def test_e2e_user_flow():
    # المستخدم يدخل أرقام
    numbers = [2, 4, 6, 8]

    # تشغيل التطبيق
    result = run_app(numbers)

    # التحقق من النتيجة النهائية
    assert "sum = 20" in result
    assert "average = 5" in result
