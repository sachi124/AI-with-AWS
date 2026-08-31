capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

# Can be reduced to:

capitalized_cities = [city.title() for cty in cities]

# conditional in list Comprehensions

squares = [x**2 for x in range(9) if x % 2 == 0]


