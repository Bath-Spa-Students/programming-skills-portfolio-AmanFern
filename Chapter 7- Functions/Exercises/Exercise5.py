#Write a function called describe_city() that accepts the name of a city and its country.

#declaring function and adding default country value
def describe_city(city, country = "Philippines"):
    msg = f"My favourite city in {country} is {city}."
    print (msg)

#calling function
describe_city(city= "Tarlac")

#cleaning up output
print ("\n")

#calling function with different city
describe_city(city= "Bacolod")

#cleaning up output
print ("\n")

#calling function with new country
describe_city("Bergen","Norway")