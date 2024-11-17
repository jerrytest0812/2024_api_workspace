# 要檢查使用者輸入的格式
# 請輸入身高(cm):xxx
# 請輸入體重(kg):xxxx
# 您的BMI是:xx
# 您的體重:xx

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

while True:
    try:
        height = float(input('請輸入身高(cm):'))
        weight = float(input('請輸入體重(kg):'))
    except ValueError:
        print('請輸入數字')
    except Exception:
        print('發生錯誤')
    else:
        bmi = weight / (height/100)**2
        status = get_status(bmi)
        print(f'體重狀態{status}')
        break
print('程式結束')

