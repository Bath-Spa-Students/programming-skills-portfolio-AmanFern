#list 5 places that you would like to visit and sort based on instructions.

#locations
place_name = ["Oslo", "Tarlac", "Makati", "Bacolod", "Munich"]
print (place_name)

#alphabetized
sort_place = sorted(place_name)
print (sort_place)

#proving list has not changed
print (place_name)

#reverse alphabetized
reverse_place = sorted(place_name, reverse=True)
print (reverse_place)

#proving list is unchanged
print (place_name)

#reversing list
place_name.reverse()
print(place_name)

#reversing list to original state
place_name.reverse()
print(place_name)

#sorting list alphabetically
place_name.sort()
print (place_name)

#sorting list reverse alphabetically
place_name.sort(reverse=True)
print (place_name)