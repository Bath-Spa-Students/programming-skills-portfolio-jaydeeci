# State the price of each USB stick and the girl's budget
usb_stick_price = 2  # Price per USB stick
budget = 17  # Total budget in pounds

# Calculate how many USB sticks she can buy
num_usb_sticks = budget // usb_stick_price  # Integer division to get the number of sticks

# Calculate how much money she will have left
money_left = budget % usb_stick_price  # Modulo operation to find the remainder

# Print the results
print(f"She can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{money_left} left.")