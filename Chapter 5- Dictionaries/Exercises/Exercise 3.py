glossary = {
    'variable': 'A value that changes depending on the conditions or information processed in the program.',
    'data': 'Any information translated in a way that it is efficient.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'tuple': "A set of unchangeable values that are separatec by commas and they store multiple data types..",
    'boolean expression': 'An expression that evaluates to True or False.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'function': 'Reusable code to perform a single and related action.',
    'control flow': 'The order where artys of a computer program - instructions, statements and function calls are executed and evaluated.
}

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
