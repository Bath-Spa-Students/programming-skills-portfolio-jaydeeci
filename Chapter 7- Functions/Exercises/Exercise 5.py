def describe_city(city, country='philippines'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('batangas')
describe_city('reykjavik', 'iceland')
describe_city('illocos')
