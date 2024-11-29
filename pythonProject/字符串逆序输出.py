def output(string,length):
    if length == 0 :
        return
    else :
        print(string[length-1],end="")
        output(string,length-1)

#str = input()
#output(str,len("string"))
