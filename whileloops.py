#1
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#2
# default_message = input("\nTell me something, and I will repeat it back to you: ")
# default_message += "\nEnter 'quit' to end the program: "
# message = ""
# active = True
# while active:
#     message = input(default_message)
#     if message == 'quit':
#         active = False
#     elif message == 'end':
#         active = False
#     elif message == 'exit':
#         active = False
#     else:
#         print(message)

#3
# question = "Please enter the name of a city you have visited:"
# input_holder =  input(question)
# place = ""
# while True:
#     place = input_holder
#     if place == 'quit':
#         break
#     print(f"I'd love to go to {input_holder}!")
#     input_holder = input(question)

#4
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)

#5
x = 1
while x <= 5:
    print(x)
    x += 1
    

 
