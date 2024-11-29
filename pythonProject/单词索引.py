tinydict = {'y':'yellow','b':'black''\n''blue','r':'red','g':'green'}
c = input()
flag = 0
for i in tinydict:
    if i == c:

       flag = 1
       print(tinydict[i])
if flag==0:
    print("Not Found")