class BMI():
    def __init__(self, name:str, height:float, weight:float):
        self.name = name
        self.height = height
        self.weight = weight

    def get_BMI(self):
        self.bmi = self.weight / (self.height/100)**2
        return self.bmi

    def get_status(self) -> str:
        bmi = self.get_BMI()
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
        name = str(input("姓名:"))
        height = float(input('請輸入身高(cm):'))
        weight = float(input('請輸入體重(kg):'))
        p1 = BMI(name=name,height=height,weight=weight)
        break 
    except Exception:
        print('輸入格式錯誤,請重新輸入!')
print(f"您的BMI值是{p1.get_BMI()}\n您的體重{p1.get_status()}")
print('程式結束')

