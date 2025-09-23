alien_color = ['green', 'yellow', 'red']
#1
color_flagging = 'green'
if color_flagging in alien_color:
    print(f"#1 You flagged {color_flagging} earned 5 points.")
else: 
    print("#1 You are failed!")

print("\n")
#2
if (color_flagging in alien_color) and color_flagging == 'green':
    print("#2 Just earned 5 points.")

elif (color_flagging in alien_color) and (color_flagging == 'yellow' or color_flagging == 'red'):
    print("#2 Just earned 10 points.")

else: 
    print("#2 You earned 1,000,000!")

print("\n")
#3
for color in alien_color:
    if (color == 'green'):
        print(f"#3 If the alien is {color}, print a message that the player earned 5 points.")
    elif color == 'yellow':
        print(f"#3 If the alien is {color}, print a message that the player earned 10 points.")
    else:
        print(f"#3 If the alien is {color}, print a message that the player earned 15 points.")

print("\n")
#4
age = 100
stage_of_life = ""
if age < 2:
    stage_of_life = "baby"
elif age >= 2 and age < 4:
    stage_of_life = "toddler"
elif age >= 4 and age < 13:
    stage_of_life = "kid"
elif age >= 13 and age < 20:
    stage_of_life = "teenager"
elif age >= 20 and age < 65:
    stage_of_life = "adult"
else:
    stage_of_life = "elder"

print(f"#4 the person is an {stage_of_life}.")

print("\n")
#5
favorite_fruits = ['apple', 'orange', 'grapes']
if 'apple' in favorite_fruits:
    print("#5 You really like apple!")

if 'orange' in favorite_fruits:
    print("#5 You really like orange!")

if 'grapes' in favorite_fruits:
    print("#5 You really like grapes!")

if ('banana' in favorite_fruits) == False:
    print("#5 Banana is not your favorite!")