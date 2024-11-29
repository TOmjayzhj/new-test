'''
def Hello_runoob():
    print('RUNOOB')

def Hello_runoobs():
    for i in range(3):
        Hello_runoob()

if __name__ == '__main__':
    Hello_runoobs()
'''

def runoob(n):
    if n == 0 :
        return
    else:
        print("RUNOOB")
        return runoob(n-1)

##n = int(input('n:'))
runoob(3)