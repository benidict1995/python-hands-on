
import operator

print("Basic Calculator")
print("* - Multiplication")
print("+ - Addition")
print("- - Substraction")
print("/ - Division")

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

print("Enter 'q' to quit.")

#1
# while True:
#     num1 = input("Give 1st number:")
#     if (num1 == 'q'):
#         break
#     num2 = input("Give 2nd number:")
#     if (num2 == 'q'):
#         break
#     operator_input = input("Operator:")
#     if  operator_input in ops:
#         try:
#             result = ops[operator_input](int(num1), int(num2))
#             print(result)
#         except ValueError:
#              print("Invalid input in num1 or num2")
#     else:
#         print("Invalid operator")
#         break

#2
while True:
    num = input("Enter number:")
    if (num == 'q'):
        break

    try:
        result = int(num)
        print(result)
    except ValueError:
        True
