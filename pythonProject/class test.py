class Test:
    num = 1
    def test(self):
        self.num += 1
        print(self.num)
'''
num = 1
a = Test()
print(num)
print(a.num)
'''
a = Test()
a.test()
print(a.num)