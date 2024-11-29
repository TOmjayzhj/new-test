for each in range(100,1000):
   i = each//100
   j = each//10%10
   k = each%10
   if each == i**3 + j**3 + k**3:
       print (each)

