#write a loop to input an age and give an appropriate ticket price for a movie

#age variable
user_age = ("What is your age? ")

#while loop
while 1 == 1 :
    age = int(input(user_age))

#setting if-elif-else statement
    if age < 3:
        print("The ticket is free for children under 3")
    elif age <=12 and age >=3 :
        print("The ticket costs $10")
    else:
        print("The ticket costs $15")
    break


