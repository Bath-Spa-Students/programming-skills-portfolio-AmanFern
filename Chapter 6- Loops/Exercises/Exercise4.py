#make a list of sandwiches and a list of finished sandwiches, run a loop to show the sandwiches being finished

#making lists
sandwich_orders = ["BLT", "Chicken Sandwich", "Nutella", "Beef sandwich"]
finished_sandwiches = []

while sandwich_orders:
    sand_ord = sandwich_orders.pop()
    print (f"{sand_ord} being prepared currently.")
    finished_sandwiches.append(sand_ord)

print ("\n")
for sandwiches in finished_sandwiches:
    print (f"{sandwiches} is ready")