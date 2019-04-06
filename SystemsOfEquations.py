import numpy as np

# First Line
num1 = input("Enter the first number of the first line: ")
num1l1 = int(num1)

num2 = input("Enter the second number of the first line: ")
num2l1 = int(num2)

num3 = input("Enter the third number of the first line: ")
num3l1 = int(num3)

num4 = input("Enter the solution of the first line: ")
soll1 = int(num4)

# Second Line
num5 = input("Enter the first number of the second line: ")
num1l2 = int(num5)

num6 = input("Enter the second number of the second line: ")
num2l2 = int(num6)

num7 = input("Enter the third number of the second line: ")
num3l2 = int(num7)

num8 = input("Enter the solution of the second line: ")
soll2 = int(num8)

# Third Line
num9 = input("Enter the first number of the third line: ")
num1l3 = int(num9)

num10 = input("Enter the second number of the third line: ")
num2l3 = int(num10)

num11 = input("Enter the third number of the third line: ")
num3l3 = int(num11)

num12 = input("Enter the solution of the third line: ")
soll3 = int(num12)

M = np.array([[num1, num2, num3], [num5, num6, num7], [num9, num10, num11]])
c = np.array([num4, num8, num12])
answer = np.linalg.solve(M, c)
print(answer)
