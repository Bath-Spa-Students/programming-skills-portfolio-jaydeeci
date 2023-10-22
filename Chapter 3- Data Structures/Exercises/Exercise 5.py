# Create a list of people to invite to dinner
guests = ["Albert Einstein", "Elvis Preseley", "Elon Musk"]

# Print the name of the guest who can't make it
guest_cant_make_it = "Elvis Preseley"
print(f"Unfortunately, {guest_cant_make_it} can't make it to dinner.")

# Replace the name of the guest who can't make it with a new person
new_guest = "Michael Jackson"
guests[guests.index(guest_cant_make_it)] = new_guest

# Print a second set of invitation messages for each person in the updated list
for guest in guests:
    invitation = f"Dear {guest}, we are inviting you over to our vacation house for dinner, this has been such a long awaited moment for us. We are looking forward to meeting you :)."
    print(invitation)