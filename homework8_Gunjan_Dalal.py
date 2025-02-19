pizza_orders = ['cheese','pepperoni','veggie','hawaiian']
finished_pizzas = []

while pizza_orders:
    current_pizza = pizza_orders.pop()
    print(f"\n{current_pizza} pizza - Your pizza pie is finished. ")
    finished_pizzas.append(current_pizza)
        
for current_pizza in finished_pizzas:
    print(f"\nThe {current_pizza} pizza was made! ")

