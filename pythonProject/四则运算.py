a = input()

if '+' in a :
    print("%.2f" % eval(a))
elif '-' in a :
    print("%.2f" % eval(a))
elif '*' in a :
    print("%.2f" % eval(a))
elif '/' in a :
    if a[-1] != '0' :
        print("%.2f" % eval(a))
    else :
        print("Divisor can not be 0！")
else :
    print("Unknown operator!")