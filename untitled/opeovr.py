class car:
    def __init__(self):
        print('noted success')
    def getinfo(self):
        print('Brand:',self.brand)
        print('Milage:',self.mil)
        print('Color',self.color)
    def default(self):
        self.brand='BMW'
        self.mil=10
        self.color='Red'
        print('value set as default')

c2=car()
c2.default()
