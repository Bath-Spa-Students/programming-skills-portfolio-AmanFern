#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.


#declaring function and adding default values
def make_shirt(size = "large", text = "I Love Python"):
    msg = f"The shirt says {text} and the size is {size}"
    print (msg)

#calling function without specifying values
make_shirt()

#cleaning up output
print ("\n")

#calling function with new size
make_shirt(size= "medium")

#cleaning up output
print ("\n")

#calling function with new size and message
make_shirt(size= "small", text= "I Love Learning")