# List of people to invite to dinner
guests = ["Albert Einstein", "Elvis Presley", "Elon Musk", "Michael Jackson"]

# Print a message that you can only invite two people
print("I can only invite two people for dinner.")

# Use pop() to remove guests from your list one at a time until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print a message to the two people still on your list
for guest in guests:
    invitation = f"Dear {guest}, you are still invited to dinner."
    print(invitation)

# Use del to remove the last two names from your list, leaving an empty list
del guests[:2]

# Print your list to confirm it's empty
print("Guest list after removing the last two names:", guests)






