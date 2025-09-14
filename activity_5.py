guests = ['ben', 'nina', 'naruto']
#for guest in guests:
 #   print(f"You are invited to the party {guest.title()}")


#print("Hi, Mr. Naruto will not be able to make it to the party, so we will replace him with Mr. Sasuke. We will send the updated guest list.\n")
guests.remove('naruto')
guests.insert(2, 'Sasuke')
#for guest in guests:
 #   print(f"You are invited to the party {guest.title()}")

print("Hi, we are happy to announce that we will be adding a new guest to the guest list. We will send the updated invitation shortly.\n")
guests.insert(0, 'hinata')
guests.insert(3, 'kiba')
guests.append('tobirama')
for guest in guests:
    print(f"Hi you are invited {guest.title()} to the party.")


print("\nHi, we will be removing some guests and will send you the updated list shortly.\n")
for guest in guests[:]:  # iterate over a copy
    if guest in ['ben', 'nina']:
        guests.remove(guest)


for newGuest in guests:
    print(f"Hi you are invited {newGuest.title()} to the party.")