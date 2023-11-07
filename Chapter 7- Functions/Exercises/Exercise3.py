#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.

#declaring function
def make_shirt(size, text):
    msg = f"The shirt says {text} and the size is {size}"
    print (msg)

#calling function using positional argument
make_shirt("medium", "I Love Dubai <3")

#break to make output look neater
print ("\n")

#calling function using keyword argument
make_shirt(text= "I Love Laufey <3", size= "extra small")