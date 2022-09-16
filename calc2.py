print("Enter the first number")
n1 = int(input())
print("Enter the second number")
n2 = int(input())
print("So! what you want?+'+,-,*,/")
n3 = input()

if n3 == '+':
    add = n1 + n2
    print(add)
elif n3 == '-':
    subtract = n1 - n2
    print(subtract)
elif n3 == '*':
    product = n1 * n2
    print(product)
elif n3 == '/':
     div = n1 / n2
     print(div)
else:
    print("not possible yet")