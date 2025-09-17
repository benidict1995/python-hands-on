for value in range(6):
    print(value)


#numbers = list(range(1, 6))
#print(f"numbers:{numbers}")

#even_numbers = list(range(2, 11, 2))
#print(f"even_numbers:{even_numbers}")

#squares = []
#for value in range (1,11):
#   squares.append(value ** 2)

#print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"min:{min(digits)}")
print(f"max:{max(digits)}")
print(f"sum:{sum(digits)}")

squares = [value**2 for value in range(1,11)]
print(f"squares:{squares}")