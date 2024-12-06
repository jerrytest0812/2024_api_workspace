#============================================================================
#Name        : biglottery.py
#撰寫一個大樂透電腦自動選號程式，程式執行會以亂數的方式顯示1-49之間七個不重複的大樂透號碼。

#============================================================

import random


class Lattory:

    def __init__(self,min= 1, max = 49,):
        self.min = min
        self.max = max
    
    def generate_lottery_number(self, number_of_lottery :int):
        if number_of_lottery > (self.max - self.min+1):
            raise ValueError("number_of_lottery exceeds the range.")
        numbers_list= random.sample(range(self.min, self.max), number_of_lottery)
        return numbers_list
    

def main():
    lattory = Lattory()
    number_of_lottery=7
    numbers_list = lattory.generate_lottery_number(number_of_lottery)
    numbers =  numbers_list
    special_num = numbers_list[-1]
    print('本期大樂透電腦選號號碼如下:')
    print(numbers)
    print(f'特別號:{special_num}')

if __name__ == '__main__':
    main()

