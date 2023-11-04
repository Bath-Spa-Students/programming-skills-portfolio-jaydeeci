def make_shirt(size='large', message='I live for the cars'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='small')
make_shirt('extra small', 'Cars are overrated')
