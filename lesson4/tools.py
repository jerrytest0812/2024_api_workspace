PI = 3.1415926

class person:
    pass

def get_status(bmi:float) -> str:
    print(f'BMI={bmi}')
    if bmi < 18.5:
        status = '過輕'
    elif bmi < 24 :
        status = '正常'
    elif bmi < 27 :
        status = '過重'
    elif bmi < 30:
        status = '輕度肥胖'
    elif bmi < 35:
        status = '中度肥胖'
    else:
        status = '重度肥胖'
    return status