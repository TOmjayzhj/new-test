string = input("input your string here :")
letters = 0
spaces = 0
digits = 0
others = 0
for i in string :
    if i.isalpha() ==  True :
        letters += 1
    elif i.isspace() == True :
        spaces += 1
    elif i.isdigit() == True :
        digits += 1
    else :
        others += 1

print('letters=%d,spaces=%d,digits=%d,others=%d\n' %
      (letters,spaces,digits,others ))