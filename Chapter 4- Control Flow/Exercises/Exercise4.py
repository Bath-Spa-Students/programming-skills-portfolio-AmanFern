#if-elif-else statement for variable age

#setting input variable
var_age = int(input ("What is your age? "))

#setting output based on input
if (var_age < 2):
    print ("You are a baby")
elif (var_age < 4):
    print ("You are a toddler")
elif (var_age < 13):
    print ("You are a kid")
elif (var_age < 20):
    print ("You are a teenager")
elif (var_age < 65):
    print ("You are an adult")
else:
    print ("You are an elder")
