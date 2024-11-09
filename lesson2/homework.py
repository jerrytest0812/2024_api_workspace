# 要檢查使用者輸入的格式
# 請輸入身高(cm):xxx
# 請輸入體重(kg):xxxx
# 您的BMI是:xx
# 您的體重:xx

try:
    height = float(input('請輸入身高(cm):'))
    print(f'身高:{height}')
    weight = float(input('請輸入體重:'))
    print(f'體重:{weight}')
except ValueError:
    print('請輸入數字')
except Exception:
    # Exeption 包含所有錯誤, 寫在最後的except
    print('發生錯誤')

else:
    bmi = weight / (height/100)**2
    print(f'BMI={bmi}')
