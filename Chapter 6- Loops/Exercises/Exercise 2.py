prompt = "How old are you?"
prompt += "\nEnter 'done' when you are done. "

while True:
    age = input(prompt)
    if age == 'done':
        break
    age = int(age)

    if age < 3:
        print("  Your ticket is free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
