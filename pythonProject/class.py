class Charact():
    等级 = 1
    经验值 = 0
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def push(self):
        print(f"{self.name}一个箭步冲向敌人！")
    def obsever(self):
        print(f"{self.name}用敏锐的眼光环顾四周")

player1 = Charact("Tom",21)
player2 = Charact("Jack",21)
print(player1.name)
print(player2.age)
print(player1.等级)
print(player2.经验值)
player1.push()
player2.obsever()