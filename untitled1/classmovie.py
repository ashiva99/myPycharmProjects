class movies:
    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine
    def info(self):
        print(self.title)
        print(self.hero)
        print(self.heroine)

li=[]
while True:
    title=input("Enter Movie Title:")
    hero=input('Enter Hero name:')
    heroine=input('Enter Heroine name:')
    m=movies(title,hero,heroine)
    li.append(m)
    option=input("Do you want to add more movies[Yes/No]:")
    if option.lower()=='no':
        break

dis=input("Do you want to display all options[Yes/No]")
if dis.lower()=='yes':
    for lis in li:
        lis.info()
        print()