import widget

def main():
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
            status = widget.get_status(bmi)
            print(f'體重狀態{status}')
            break
    print('程式結束')

if __name__ == '__main__':
    main()

