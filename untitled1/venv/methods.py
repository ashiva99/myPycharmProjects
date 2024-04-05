class car:
    wheels = 4
    def __init__(self,cmp,model,mil):
        self.cmp=cmp
        self.model=model
        self.mil=mil
        print('object has been created')
    def change(self):
        self.mil=8
    @classmethod
    def info(cls):
        return cls.wheels
    def abt():
        print('This is about car')

s1=car('bmw',2018,12)
s1.wheels=5
print(s1.model)
print(car.info())
print(s1.wheels)
print(car.info())
print(car.abt())