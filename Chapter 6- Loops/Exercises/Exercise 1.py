prompt = "\nWhat type of pizza do you want?"
prompt += "\nEnter 'done' when you are done: "

while True:
    pizza = input(prompt)
    if topping != 'done':
        print("  I'll add " + pizza + " to your order.")
    else:
        break
