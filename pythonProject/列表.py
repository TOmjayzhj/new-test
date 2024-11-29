'''
a = [1,2,3,4]
print(len(a))
print(a[2:])
a.append(5)
print(len(a))
print(a[-1])
a.pop(4)
print(len(a))
'''
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][2])
col2 = [row[2] for row in matrix]
print(col2)
col1 = [row[1] for row in matrix if row[1]%2 == 0]
print(col1)