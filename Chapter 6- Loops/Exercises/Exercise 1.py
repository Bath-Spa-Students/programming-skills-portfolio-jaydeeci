prompt = "\nWhat type of pizza topping do you want?"
prompt += "\nEnter 'done' when you are done: "

while True:
    pizza = input(prompt)
    if topping != 'done':
        print("  I'll add " + toppings + " to your pizza.")
    else:
        break
