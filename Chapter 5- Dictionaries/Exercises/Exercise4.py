#using a dictionary, store information of 3 major rivers
#use loops to print


#creating dictionary
major_rivers = {'The Yangtze' : 'China',
                'The Indus' : 'South and Central Asia',
                'The Danube' : 'Central and Southeastern Europe'}

#print loop for each river and its location
for name in major_rivers.keys():
    print(f"{name.title()} flows through {major_rivers[name]} \n")

#printing each river name
print ("These three major rivers are called:")
for name in major_rivers.keys():
    print (name.title())

print("\n")

#printing the locations
print ("The places these rivers run through are:")
for location in major_rivers.keys():
    print (location.title())