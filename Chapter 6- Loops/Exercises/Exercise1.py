#write a loop to enter pizza toppings
#after each input write that the topping will be added

#making list
topping_list = []

print ("type end to finish adding toppings")
#while loop for inputting toppings
while 1 == 1:
    pizza_toppings = input("Enter a pizza topping: ").strip()

#setting a break for the loop and using append to add toppings into list
    if pizza_toppings.lower() == 'end':
        break  
    else:
        topping_list.append(pizza_toppings)
        print(f"{pizza_toppings} will be added to your pizza.")

#printing all toppings added
print("Your pizza be topped with:", topping_list)
