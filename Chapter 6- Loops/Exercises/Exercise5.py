#using the code from exercise 4, add pastrami to the list 3 times
#remove all pastrami from list using while loop

#pastrami message
print ("The deli has run out of pastrami.")

#making lists
sandwich_orders = ["BLT", "Pastrami", "Chicken Sandwich", "Pastrami", "Nutella", "Beef sandwich", "Pastrami"]
finished_sandwiches = []

while "Pastrami" in sandwich_orders:
     sandwich_orders.remove("Pastrami")

while sandwich_orders:
        sand_ord = sandwich_orders.pop()
        print (f"{sand_ord} being prepared currently.")
        finished_sandwiches.append(sand_ord)


print ("\n")
for sandwiches in finished_sandwiches:
    print (f"{sandwiches} is ready")