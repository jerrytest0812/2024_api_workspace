class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
    
    def echo(self):
        print(f'name:{self.name}')
        print(f'age:{self.age}')


class Student(Person):
    def __init__(self,name:str, age:int, score:int):
        super().__init__(name=name, age=age)
        self.__score = score

    @property
    def score(self)->int:
        return self.__score
    
    def echo(self):
        super().echo()
        print(f'score:{self.score}')